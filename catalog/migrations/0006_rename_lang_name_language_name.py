# Generated by Django 4.0.5 on 2022-06-21 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_author_date_of_death'),
    ]

    operations = [
        migrations.RenameField(
            model_name='language',
            old_name='lang_name',
            new_name='name',
        ),
    ]
