# Generated by Django 3.1.6 on 2021-02-18 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watches', '0003_auto_20210219_0131'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='watch',
            options={'ordering': ('-updated_at',)},
        ),
        migrations.RemoveField(
            model_name='watch',
            name='name',
        ),
    ]
