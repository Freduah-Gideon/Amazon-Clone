# Generated by Django 2.2.14 on 2020-09-23 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20200923_1754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='promo_code',
            new_name='coupon',
        ),
    ]