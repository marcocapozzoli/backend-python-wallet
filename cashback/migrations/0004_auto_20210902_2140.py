# Generated by Django 3.2.6 on 2021-09-03 00:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cashback', '0003_auto_20210902_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='amount',
            field=models.FloatField(verbose_name='Total'),
        ),
        migrations.AlterField(
            model_name='buy',
            name='cashback',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='buy',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Sale date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]