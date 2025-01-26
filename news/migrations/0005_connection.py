# Generated by Django 5.1.5 on 2025-01-25 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_gallery_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
                ('working_hours', models.CharField(max_length=255)),
                ('first_phone', models.CharField(max_length=20)),
                ('second_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('embed_map_html', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
