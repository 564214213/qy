# Generated by Django 2.1.4 on 2020-04-23 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200423_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='jinhuo',
            name='color',
            field=models.CharField(max_length=6, null=True, verbose_name='颜色'),
        ),
        migrations.AddField(
            model_name='jinhuo',
            name='price',
            field=models.IntegerField(default=0, verbose_name='单价'),
        ),
        migrations.AddField(
            model_name='jinhuo',
            name='price_total',
            field=models.IntegerField(default=0, verbose_name='总价'),
        ),
        migrations.AddField(
            model_name='kucun',
            name='color',
            field=models.CharField(max_length=6, null=True, verbose_name='颜色'),
        ),
        migrations.AddField(
            model_name='kucun',
            name='price',
            field=models.IntegerField(default=0, verbose_name='单价'),
        ),
        migrations.AddField(
            model_name='kucun',
            name='price_total',
            field=models.IntegerField(default=0, verbose_name='总价'),
        ),
        migrations.AddField(
            model_name='xiaoshou',
            name='color',
            field=models.CharField(max_length=6, null=True, verbose_name='颜色'),
        ),
        migrations.AlterField(
            model_name='jinhuo',
            name='c_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='jinhuo',
            name='l_total',
            field=models.IntegerField(default=0, verbose_name='L'),
        ),
        migrations.AlterField(
            model_name='jinhuo',
            name='m_total',
            field=models.IntegerField(default=0, verbose_name='M'),
        ),
        migrations.AlterField(
            model_name='jinhuo',
            name='number',
            field=models.CharField(max_length=10, verbose_name='商品款号'),
        ),
        migrations.AlterField(
            model_name='jinhuo',
            name='sort',
            field=models.CharField(max_length=10, verbose_name='商品名称'),
        ),
        migrations.AlterField(
            model_name='jinhuo',
            name='total',
            field=models.IntegerField(default=0, verbose_name='总数'),
        ),
        migrations.AlterField(
            model_name='jinhuo',
            name='xl_total',
            field=models.IntegerField(default=0, verbose_name='XL'),
        ),
        migrations.AlterField(
            model_name='jinhuo',
            name='xxl_total',
            field=models.IntegerField(default=0, verbose_name='2XL'),
        ),
        migrations.AlterField(
            model_name='jinhuo',
            name='xxxl_total',
            field=models.IntegerField(default=0, verbose_name='3XL'),
        ),
        migrations.AlterField(
            model_name='jinhuo',
            name='xxxxl_total',
            field=models.IntegerField(default=0, verbose_name='4XL'),
        ),
        migrations.AlterField(
            model_name='kucun',
            name='l_total',
            field=models.IntegerField(default=0, verbose_name='L'),
        ),
        migrations.AlterField(
            model_name='kucun',
            name='m_total',
            field=models.IntegerField(default=0, verbose_name='M'),
        ),
        migrations.AlterField(
            model_name='kucun',
            name='number',
            field=models.CharField(max_length=8, verbose_name='商品款号'),
        ),
        migrations.AlterField(
            model_name='kucun',
            name='sort',
            field=models.CharField(max_length=10, verbose_name='商品名称'),
        ),
        migrations.AlterField(
            model_name='kucun',
            name='xl_total',
            field=models.IntegerField(default=0, verbose_name='XL'),
        ),
        migrations.AlterField(
            model_name='kucun',
            name='xxl_total',
            field=models.IntegerField(default=0, verbose_name='2XL'),
        ),
        migrations.AlterField(
            model_name='kucun',
            name='xxxl_total',
            field=models.IntegerField(default=0, verbose_name='3XL'),
        ),
        migrations.AlterField(
            model_name='kucun',
            name='xxxxl_total',
            field=models.IntegerField(default=0, verbose_name='4XL'),
        ),
        migrations.AlterField(
            model_name='xiaoshou',
            name='l_total',
            field=models.IntegerField(default=0, verbose_name='L'),
        ),
        migrations.AlterField(
            model_name='xiaoshou',
            name='m_total',
            field=models.IntegerField(default=0, verbose_name='M'),
        ),
        migrations.AlterField(
            model_name='xiaoshou',
            name='number',
            field=models.CharField(max_length=10, verbose_name='商品款号'),
        ),
        migrations.AlterField(
            model_name='xiaoshou',
            name='sort',
            field=models.CharField(max_length=10, verbose_name='商品名称'),
        ),
        migrations.AlterField(
            model_name='xiaoshou',
            name='xiaoshou_total',
            field=models.IntegerField(default=0, verbose_name='总数'),
        ),
        migrations.AlterField(
            model_name='xiaoshou',
            name='xl_total',
            field=models.IntegerField(default=0, verbose_name='XL'),
        ),
        migrations.AlterField(
            model_name='xiaoshou',
            name='xxl_total',
            field=models.IntegerField(default=0, verbose_name='2XL'),
        ),
        migrations.AlterField(
            model_name='xiaoshou',
            name='xxxl_total',
            field=models.IntegerField(default=0, verbose_name='3XL'),
        ),
        migrations.AlterField(
            model_name='xiaoshou',
            name='xxxxl_total',
            field=models.IntegerField(default=0, verbose_name='4XL'),
        ),
    ]
