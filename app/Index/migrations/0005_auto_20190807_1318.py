# Generated by Django 2.1.4 on 2019-08-07 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0004_auto_20190807_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='buy_user_id',
            field=models.IntegerField(default=0),
        ),
    ]
