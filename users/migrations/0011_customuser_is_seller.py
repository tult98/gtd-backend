# Generated by Django 3.1.6 on 2021-03-14 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20210314_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_seller',
            field=models.BooleanField(default=False),
        ),
    ]