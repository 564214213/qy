# Generated by Django 2.1.4 on 2021-03-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20210321_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jinhuo',
            name='number',
            field=models.CharField(max_length=4096, verbose_name='商品款号'),
        ),
        migrations.AlterField(
            model_name='jinhuo',
            name='sort',
            field=models.CharField(max_length=10, verbose_name='商品名称'),
        ),
    ]
