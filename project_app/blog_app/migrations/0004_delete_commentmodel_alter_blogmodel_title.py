# Generated by Django 4.2.2 on 2023-06-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_commentmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='commentModel',
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]