# Generated by Django 3.2.4 on 2021-06-28 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user_profile',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='review',
            name='review_body',
            field=models.CharField(default='', max_length=400),
        ),
    ]
