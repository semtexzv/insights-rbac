# Generated by Django 2.1.5 on 2019-04-07 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_remove_principal_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='system',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='role',
            name='version',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
