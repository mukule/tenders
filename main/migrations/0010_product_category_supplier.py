# Generated by Django 4.2.2 on 2023-06-09 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_citizencontractor_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('duns_number', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=50)),
                ('tax_jurisdiction_code', models.CharField(max_length=50)),
                ('currency', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('region_district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('company_postal_code', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=100)),
                ('building', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=100)),
                ('function', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product_category')),
                ('vendor_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
    ]
