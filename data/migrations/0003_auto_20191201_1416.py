# Generated by Django 2.2.7 on 2019-12-01 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20191129_2229'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tweet',
            unique_together=set(),
        ),
    ]
