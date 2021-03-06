# Generated by Django 2.2.7 on 2019-12-01 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20191201_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(default='2019-01-01 00:00:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='twitteruser',
            name='username',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterUniqueTogether(
            name='tweet',
            unique_together={('username', 'created_at')},
        ),
    ]
