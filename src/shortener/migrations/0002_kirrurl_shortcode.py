# Generated by Django 4.1 on 2022-09-08 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(default='cfedefaultshortcode', max_length=15),
            preserve_default=False,
        ),
    ]