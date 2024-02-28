# Generated by Django 4.2.7 on 2024-02-22 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reportage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(upload_to='reportage/images')),
                ('image_2', models.ImageField(blank=True, upload_to='reportage/images')),
                ('image_3', models.ImageField(blank=True, upload_to='reportage/images')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reportages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'گزارش',
                'verbose_name_plural': '  گزارش ها',
            },
        ),
    ]
