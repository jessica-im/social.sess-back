# Generated by Django 3.2.9 on 2021-11-18 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions_api', '0005_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='comment',
            field=models.ManyToManyField(to='questions_api.Comment'),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='comment',
            field=models.ManyToManyField(to='questions_api.Comment'),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='question',
            field=models.ManyToManyField(to='questions_api.Question'),
        ),
    ]
