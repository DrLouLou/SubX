# Generated by Django 3.0.8 on 2020-07-22 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_auto_20200718_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='steps',
            field=models.TextField(null=True),
        ),
    ]
