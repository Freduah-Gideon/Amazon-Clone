# Generated by Django 2.2.14 on 2020-09-18 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('category', models.CharField(blank=True, choices=[('Electronics', 'Electronics'), ('computers', 'Computers')], max_length=200, null=True)),
                ('sub_category', models.CharField(blank=True, choices=[('camera_and_photo', 'Camera & Photo'), ('laptops', 'Laptops')], max_length=200, null=True)),
                ('in_stock', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('features', models.ManyToManyField(to='products.Features')),
            ],
        ),
    ]