# Generated by Django 5.0 on 2023-12-27 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PaperHub', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moderator',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='moderator',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='paperhubuser',
            name='favorite_articles',
        ),
        migrations.RemoveField(
            model_name='paperhubuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='paperhubuser',
            name='saved_articles',
        ),
        migrations.RemoveField(
            model_name='paperhubuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='Moderator',
        ),
        migrations.DeleteModel(
            name='PaperHubUser',
        ),
    ]