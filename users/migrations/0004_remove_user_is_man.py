# Generated by Django 3.0 on 2019-12-12 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191211_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_man',
        ),
    ]
