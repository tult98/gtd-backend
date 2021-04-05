from django.urls import path, re_path
from products import views

urlpatterns = [
    path(
        'products/',
        views.ProductList.as_view(),
        name=views.ProductList.name
    ),
    re_path(
        'products/(?P<pk>[0-9]+)$',
        views.ProductDetailDisplay.as_view(),
        name=views.ProductDetailDisplay.name
    ),
    re_path(
        'products/(?P<pk>[0-9]+)/manage$',
        views.ProductDetailManage.as_view(),
        name=views.ProductDetailManage.name
    ),
    re_path(
        'products/(?P<pk>[0-9]+)/update$',
        views.ProductUpdate.as_view(),
        name=views.ProductUpdate.name
    ),
    re_path(
        'products/(?P<pk>[0-9]+)/destroy$',
        views.ProductDestroy.as_view(),
        name=views.ProductDestroy.name
    ),
    path(
        'check-price/',
        views.CheckPrice.as_view(),
        name=views.CheckPrice.name
    ),
    path(
        'sellers/',
        views.SellerList.as_view(),
        name=views.SellerList.name
    ),
    re_path(
        'sellers/(?P<pk>[0-9]+)$',
        views.SellerDetail.as_view(),
        name=views.SellerDetail.name
    ),
    re_path(
        'sellers/(?P<pk>[0-9]+)/update$',
        views.SellerUpdate.as_view(),
        name=views.SellerUpdate.name
    ),
    re_path(
        'sellers/(?P<pk>[0-9]+)/destroy$',
        views.SellerDestroy.as_view(),
        name=views.SellerDestroy.name
    ),
    path(
        'products/search',
        views.SearchProduct.as_view(),
        name=views.SearchProduct.name
    ),
]
