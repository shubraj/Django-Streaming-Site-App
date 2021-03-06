# Generated by Django 3.1.2 on 2021-01-02 12:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApkVersionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_code', models.IntegerField(default=1)),
                ('version_name', models.CharField(default='v1.0.0', max_length=5)),
                ('whats_new', models.TextField()),
                ('apk_url', models.URLField()),
                ('is_skipable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_symbol', models.CharField(default='$', max_length=4)),
                ('currency', models.CharField(blank=True, max_length=8)),
                ('exchnage_rate', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5000)])),
                ('paypal_enable', models.BooleanField(default=False)),
                ('paypal_email', models.EmailField(default='john@cena.com', max_length=30)),
                ('paypal_client_id', models.CharField(blank=True, max_length=200, null=True)),
                ('stripe_enable', models.BooleanField(default=False)),
                ('stripe_publishable_key', models.CharField(blank=True, max_length=200, null=True)),
                ('stripe_secret_key', models.CharField(blank=True, max_length=200, null=True)),
                ('razorpay_enable', models.BooleanField(default=False)),
                ('razorpay_key_id', models.CharField(blank=True, max_length=200, null=True)),
                ('razorpay_key_secret', models.CharField(max_length=200, null=True)),
                ('razorpay_inr_exchange_rate', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5000)])),
            ],
        ),
    ]
