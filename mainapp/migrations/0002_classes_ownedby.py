# Generated by Django 3.1 on 2020-08-10 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='ownedby',
            field=models.CharField(default='ok', max_length=15),
            preserve_default=False,
        ),
    ]
