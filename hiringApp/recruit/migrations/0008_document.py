# Generated by Django 3.1.6 on 2021-08-18 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0007_auto_20210215_0640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='documents')),
            ],
        ),
    ]