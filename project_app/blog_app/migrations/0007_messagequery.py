# Generated by Django 4.2.2 on 2023-09-15 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_remove_commentmodel_commented_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='messageQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
    ]