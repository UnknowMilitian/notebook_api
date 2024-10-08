# Generated by Django 5.1.1 on 2024-09-04 00:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0004_postview'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255, verbose_name='Fullname')),
                ('info', models.CharField(max_length=255, verbose_name='Info')),
                ('facebook', models.CharField(blank=True, max_length=255, null=True, verbose_name='Facebook')),
                ('twitter', models.CharField(blank=True, max_length=255, null=True, verbose_name='Twitter')),
                ('instagram', models.CharField(blank=True, max_length=255, null=True, verbose_name='Instagram')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='PostView',
        ),
    ]
