# Generated by Django 3.2.8 on 2021-11-08 11:44

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0015_auto_20211108_0858'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='artist',
            managers=[
                ('artists', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterOrderWithRespectTo(
            name='song',
            order_with_respect_to='album',
        ),
    ]