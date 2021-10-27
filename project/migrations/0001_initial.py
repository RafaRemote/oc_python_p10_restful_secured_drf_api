# Generated by Django 3.2.8 on 2021-10-27 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('TYPE_1', 'type_1'), ('TYPE_2', 'type_2'), ('TYPE_3', 'type_3')], max_length=100)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
