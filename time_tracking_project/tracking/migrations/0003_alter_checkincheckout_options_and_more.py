# Generated by Django 4.2.13 on 2024-07-14 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_checkincheckout'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checkincheckout',
            options={},
        ),
        migrations.AlterField(
            model_name='checkincheckout',
            name='check_in_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='checkincheckout',
            name='total_hours',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
