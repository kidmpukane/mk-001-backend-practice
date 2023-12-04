# Generated by Django 4.2.4 on 2023-12-04 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=225)),
                ('store_description', models.CharField(max_length=225)),
                ('store_image', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('merchant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profiles.merchant')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]