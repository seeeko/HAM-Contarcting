# Generated by Django 2.2.1 on 2019-08-25 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190825_2353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='create_date',
        ),
    ]
