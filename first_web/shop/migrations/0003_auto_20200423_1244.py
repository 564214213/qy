# Generated by Django 2.1.4 on 2020-04-23 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200423_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='xiaoshou',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=12, unique=True, verbose_name='服装款号')),
                ('sort', models.CharField(max_length=6, verbose_name='类别')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='出售时间')),
                ('size', models.CharField(choices=[('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('xxl', '2XL'), ('xxxl', '3XL'), ('xxxxl', '4XL')], max_length=4, verbose_name='尺码')),
                ('xiaoshou_total', models.IntegerField(default=0, verbose_name='出售件数')),
            ],
            options={
                'verbose_name': '销售',
                'verbose_name_plural': '销售',
                'ordering': ['-c_time'],
            },
        ),
        migrations.AlterField(
            model_name='jinhuo',
            name='l_total',
            field=models.IntegerField(default=0, verbose_name='L号的总数'),
        ),
        migrations.AlterField(
            model_name='jinhuo',
            name='m_total',
            field=models.IntegerField(default=0, verbose_name='M号的总数'),
        ),
        migrations.AlterField(
            model_name='jinhuo',
            name='total',
            field=models.IntegerField(default=0, verbose_name='进货总数'),
        ),
        migrations.AlterField(
            model_name='jinhuo',
            name='xl_total',
            field=models.IntegerField(default=0, verbose_name='XL号的总数'),
        ),
        migrations.AlterField(
            model_name='jinhuo',
            name='xxl_total',
            field=models.IntegerField(default=0, verbose_name='2XL号的总数'),
        ),
        migrations.AlterField(
            model_name='jinhuo',
            name='xxxl_total',
            field=models.IntegerField(default=0, verbose_name='3XL号的总数'),
        ),
        migrations.AlterField(
            model_name='jinhuo',
            name='xxxxl_total',
            field=models.IntegerField(default=0, verbose_name='4XL号的总数'),
        ),
    ]
