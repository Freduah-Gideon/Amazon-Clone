# Generated by Django 2.2.14 on 2020-09-24 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
