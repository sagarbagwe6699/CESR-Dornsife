# Generated by Django 4.0.2 on 2022-02-16 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0005_thread_infographic'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='infographic_link',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='thread',
            name='infographic',
            field=models.TextField(default='', max_length=255),
        ),
    ]
