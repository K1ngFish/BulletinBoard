# Generated by Django 4.2.3 on 2023-07-17 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0007_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]