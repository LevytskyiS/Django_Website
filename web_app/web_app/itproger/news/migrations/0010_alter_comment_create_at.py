# Generated by Django 4.2.2 on 2023-07-08 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_comment_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
