# Generated by Django 4.0.4 on 2022-05-06 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0009_post_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(default='your text'),
        ),
    ]
