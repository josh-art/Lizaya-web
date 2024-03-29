# Generated by Django 2.2.14 on 2024-02-26 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True)),
                ('message', models.TextField(max_length=300)),
                ('submitted_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('submitted_date',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='post_pics')),
                ('body', models.TextField(blank=True)),
                ('caption', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
