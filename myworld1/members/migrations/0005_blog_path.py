# Generated by Django 4.2.1 on 2023-05-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='path',
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
    ]
