# Generated by Django 4.2.2 on 2023-07-22 13:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_alter_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]