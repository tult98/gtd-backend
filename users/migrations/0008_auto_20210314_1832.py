# Generated by Django 3.1.6 on 2021-03-14 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_customuser_is_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_seller',
            field=models.BooleanField(default=False),
        ),
    ]
