# Generated by Django 4.2.2 on 2023-07-03 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='copy',
            name='number_copies',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]