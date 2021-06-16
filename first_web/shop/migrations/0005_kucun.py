# Generated by Django 2.1.4 on 2020-04-23 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200423_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='kucun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=12, unique=True, verbose_name='服装款号')),
                ('sort', models.CharField(max_length=6, verbose_name='类别')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='库存更新时间')),
                ('m_total', models.IntegerField(default=0, verbose_name='M号的总数')),
                ('l_total', models.IntegerField(default=0, verbose_name='L号的总数')),
                ('xl_total', models.IntegerField(default=0, verbose_name='XL号的总数')),
                ('xxl_total', models.IntegerField(default=0, verbose_name='2XL号的总数')),
                ('xxxl_total', models.IntegerField(default=0, verbose_name='3XL号的总数')),
                ('xxxxl_total', models.IntegerField(default=0, verbose_name='4XL号的总数')),
                ('total', models.IntegerField(default=0, verbose_name='库存总数')),
            ],
            options={
                'verbose_name': '库存',
                'verbose_name_plural': '库存',
                'ordering': ['-c_time'],
            },
        ),
    ]
