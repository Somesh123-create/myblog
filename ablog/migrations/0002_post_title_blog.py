# Generated by Django 3.1.7 on 2021-02-24 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ablog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_blog',
            field=models.CharField(default='My Blog', max_length=255),
        ),
    ]