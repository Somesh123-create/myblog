# Generated by Django 3.1.7 on 2021-05-25 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ablog', '0013_auto_20210520_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ablog.category'),
        ),
    ]