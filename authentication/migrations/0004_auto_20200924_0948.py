# Generated by Django 2.2.14 on 2020-09-24 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20200924_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]