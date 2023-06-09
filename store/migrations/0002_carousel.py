# Generated by Django 4.1.7 on 2023-03-13 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(null='True', upload_to='media')),
                ('description', models.TextField(blank=True)),
                ('rank', models.IntegerField()),
            ],
        ),
    ]
