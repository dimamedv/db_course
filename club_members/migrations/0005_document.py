# Generated by Django 5.0 on 2024-01-12 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_members', '0004_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('pdf_data', models.BinaryField(verbose_name='PDF Файл')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
    ]