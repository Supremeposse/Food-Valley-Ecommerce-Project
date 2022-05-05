# Generated by Django 3.2.9 on 2022-04-12 01:35

import cloudinary.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created Datetime'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, default=99.99, max_digits=11, verbose_name='Price'),
        ),
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('deleted', 'Deleted')], db_index=True, default='draft', max_length=50, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='item',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Datetime'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(db_index=True, default='anonymous', max_length=120, verbose_name='Name'),
        ),
    ]
