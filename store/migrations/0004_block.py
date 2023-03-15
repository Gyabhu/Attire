# Generated by Django 4.1.7 on 2023-03-13 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_carousel_description_carousel_title1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(null='True', upload_to='media')),
                ('description', models.CharField(max_length=300, null='True')),
            ],
        ),
    ]
