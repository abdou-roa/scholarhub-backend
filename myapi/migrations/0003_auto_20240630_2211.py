# Generated by Django 2.1.5 on 2024-06-30 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20240629_0105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='topic',
            new_name='topic_id',
        ),
    ]
