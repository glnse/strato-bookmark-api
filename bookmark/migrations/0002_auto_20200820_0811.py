# Generated by Django 3.1 on 2020-08-20 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmark',
            options={},
        ),
        migrations.RenameField(
            model_name='bookmark',
            old_name='code',
            new_name='url',
        ),
    ]
