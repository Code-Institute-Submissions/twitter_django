# Generated by Django 2.2.7 on 2019-11-29 22:21

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
            ],
            options={
                'unique_together': {('username',)},
            },
        ),
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.TwitterUser')),
            ],
            options={
                'unique_together': {('username',)},
            },
        ),
    ]