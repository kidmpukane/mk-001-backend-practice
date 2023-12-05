# Generated by Django 4.2.4 on 2023-12-05 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profiles', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TertiaryCollection',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('collection_title', models.CharField(max_length=25)),
                ('collection_image', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.store')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SecondaryCollection',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('collection_title', models.CharField(max_length=25)),
                ('collection_image', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.store')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PrimaryCollection',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('collection_title', models.CharField(max_length=25)),
                ('collection_image', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.store')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerCollection',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('collection_title', models.CharField(max_length=25)),
                ('collection_image', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profiles.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
