from rest_framework.permissions import IsAuthenticated
from gtd_backend.custompermission import IsAdmin, IsAdminOrOwner
from rest_framework import generics
from products.models import (
    Product,
    Seller,
    Brand,
    Category,
    Image,
)
from products.serializers import (
    ProductCreateSerializer, ProductSerializer, SellerSerializer
)
from rest_framework.response import Response
from rest_framework import serializers
from gtd_backend.utils import get_product_data, product_data_for_create, shorten_product_data, shorten_seller_data, update_or_create_brand, update_or_create_category, update_or_create_images, update_or_create_product, update_or_create_seller
from rest_framework import status
# Create your views here.


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated, IsAdmin,)
    name = 'product-list'

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return ProductCreateSerializer
        return ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product_id = serializer.data.get('product_id')

        product_data = get_product_data(product_id)

        brand = update_or_create_brand(product_data)
        seller = update_or_create_seller(product_data)
        category = update_or_create_category(product_data)

        product = update_or_create_product(
            product_data, brand, category, seller)

        update_or_create_images(product_data, product)

        product_serializer = ProductSerializer(instance=product)
        return Response(product_serializer.data)


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    name = 'product-detail'

    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        try:
            product = Product.objects.get(pk=product_id)
        except:
            product = None
        # current user is Admin
        if self.request.user.profile.role == 3:
            if not product:
                raise serializers.ValidationError({'detail': 'Not found'})
            return super().get(request, *args, **kwargs)
        # current user is normal user
        else:
            if not product:
                product_data = get_product_data(product_id)
                brief_product_data = shorten_product_data(product_data)
                return Response(brief_product_data)
            else:
                return super().get(request, *args, **kwargs)


class ProductUpdate(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name = 'product-update'

    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        try:
            product = Product.objects.get(pk=product_id)
            product_data = get_product_data(product_id)

            brand = update_or_create_brand(product_data)
            seller = update_or_create_seller(product_data)
            category = update_or_create_category(product_data)

            product = update_or_create_product(
                product_data, brand, category, seller)

            update_or_create_images(product_data, product)

            return Response(shorten_product_data(product_data), status=status.HTTP_200_OK)

        except:
            raise serializers.ValidationError({'detail': 'Not found'})


class ProductDestroy(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, IsAdmin)
    name = 'product-destroy'


class SellerList(generics.ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    name = 'seller-list'

    def create(self, request, *args, **kwargs):
        if (self.request.user.profile.role != 3):
            raise serializers.ValidationError(
                {'detail': 'You do not have permission to perform this action'})
        return super().create(request, *args, **kwargs)


class SellerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = (IsAuthenticated)
    name = 'seller-detail'
