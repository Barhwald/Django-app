# Generated by Django 4.0.4 on 2022-05-06 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_alter_post_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=140),
        ),
    ]
