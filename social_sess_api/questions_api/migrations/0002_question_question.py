# Generated by Django 3.2.9 on 2021-11-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]
