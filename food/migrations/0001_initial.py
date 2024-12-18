# Generated by Django 5.1.1 on 2024-11-09 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category_name', models.CharField(max_length=100)),
                ('category_image', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='products/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('stock_quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]
