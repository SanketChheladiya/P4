# Generated by Django 3.2.8 on 2021-10-28 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthdate',
            field=models.CharField(max_length=10),
        ),
    ]
