# Generated by Django 2.1.4 on 2021-03-21 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20210321_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jinhuo',
            name='number',
            field=models.CharField(max_length=30, verbose_name='商品款号'),
        ),
        migrations.AlterField(
            model_name='jinhuo',
            name='sort',
            field=models.CharField(max_length=30, verbose_name='商品名称'),
        ),
    ]
