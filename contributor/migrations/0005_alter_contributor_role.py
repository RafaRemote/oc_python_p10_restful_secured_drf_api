# Generated by Django 3.2.8 on 2021-11-04 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributor', '0004_auto_20211103_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='role',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
