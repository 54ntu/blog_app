# Generated by Django 4.2.2 on 2023-06-10 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_commentmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentmodel',
            name='commented_at',
        ),
    ]
