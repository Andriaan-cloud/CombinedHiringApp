# Generated by Django 3.1.6 on 2021-09-09 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0013_delete_cvtemplate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='social',
            field=models.CharField(choices=[('Facebook', 'Facebook'), ('LinkedIn', 'LinkedIn'), ('Twitter', 'Twitter'), ('Google+', 'Google+'), ('Email', 'Email'), ('Mindworx Website', 'Mindworx Website')], max_length=150, null=True),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
