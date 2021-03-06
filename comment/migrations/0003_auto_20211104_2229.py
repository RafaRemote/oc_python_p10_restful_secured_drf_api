# Generated by Django 3.2.8 on 2021-11-04 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0005_auto_20211104_2132'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='issue_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='issue.issue'),
        ),
    ]
