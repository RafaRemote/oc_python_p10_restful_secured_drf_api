# Generated by Django 3.2.8 on 2021-10-27 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('ADMIN', 'admin'), ('CONTRIB', 'contrib')], default='p1', max_length=100)),
                ('role', models.CharField(choices=[('r1', 'r1'), ('r2', 'r2'), ('r3', 'r3')], default='r1', max_length=100)),
            ],
        ),
    ]
