# Generated by Django 4.2.4 on 2023-12-12 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_primaryproduct_feature_list_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primaryproduct',
            name='feature_list',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='secondaryproduct',
            name='feature_list',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tertiaryproduct',
            name='feature_list',
            field=models.BigIntegerField(null=True),
        ),
    ]
