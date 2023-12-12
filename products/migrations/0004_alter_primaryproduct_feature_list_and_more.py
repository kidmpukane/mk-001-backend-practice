# Generated by Django 4.2.4 on 2023-12-12 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_primaryproduct_feature_list_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primaryproduct',
            name='feature_list',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='secondaryproduct',
            name='feature_list',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='tertiaryproduct',
            name='feature_list',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
