# Generated by Django 3.2.7 on 2021-09-16 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('timestamp',)},
        ),
    ]