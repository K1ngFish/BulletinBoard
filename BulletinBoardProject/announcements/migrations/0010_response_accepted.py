# Generated by Django 4.2.3 on 2023-07-21 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0009_alter_response_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]