# Generated by Django 3.1.6 on 2021-03-06 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ablog', '0008_auto_20210306_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Above To Read The Blog Posts....', max_length=255),
        ),
    ]