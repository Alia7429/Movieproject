# Generated by Django 3.2.15 on 2022-09-10 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nextapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='fhtdyt', upload_to='pics'),
            preserve_default=False,
        ),
    ]
