# Generated by Django 3.1.6 on 2021-02-12 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='responsibilitie',
            new_name='responsibilities',
        ),
    ]