# Generated by Django 2.1.4 on 2020-04-23 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200423_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xiaoshou',
            name='size',
        ),
        migrations.AddField(
            model_name='xiaoshou',
            name='l_total',
            field=models.IntegerField(default=0, verbose_name='出售L号/件'),
        ),
        migrations.AddField(
            model_name='xiaoshou',
            name='m_total',
            field=models.IntegerField(default=0, verbose_name='出售M号/件'),
        ),
        migrations.AddField(
            model_name='xiaoshou',
            name='xl_total',
            field=models.IntegerField(default=0, verbose_name='出售XL号/件'),
        ),
        migrations.AddField(
            model_name='xiaoshou',
            name='xxl_total',
            field=models.IntegerField(default=0, verbose_name='出售2XL号/件'),
        ),
        migrations.AddField(
            model_name='xiaoshou',
            name='xxxl_total',
            field=models.IntegerField(default=0, verbose_name='出售3XL号/件'),
        ),
        migrations.AddField(
            model_name='xiaoshou',
            name='xxxxl_total',
            field=models.IntegerField(default=0, verbose_name='出售4XL号/件'),
        ),
        migrations.AlterField(
            model_name='xiaoshou',
            name='xiaoshou_total',
            field=models.IntegerField(default=0, verbose_name='出售总件数'),
        ),
    ]
