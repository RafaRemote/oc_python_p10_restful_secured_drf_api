# Generated by Django 3.2.8 on 2021-11-04 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributor', '0011_alter_contributor_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='permission',
            field=models.CharField(blank=True, choices=[('AUTHOR', 'author'), ('CONTRIBUTOR', 'contributor')], max_length=11, null=True),
        ),
    ]
