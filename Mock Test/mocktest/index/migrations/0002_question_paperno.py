# Generated by Django 2.0.2 on 2018-03-06 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='paperno',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
