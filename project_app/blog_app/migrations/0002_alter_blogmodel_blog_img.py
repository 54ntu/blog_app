# Generated by Django 4.2.2 on 2023-06-09 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='blog_img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]