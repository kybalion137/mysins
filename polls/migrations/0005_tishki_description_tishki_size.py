# Generated by Django 4.2 on 2023-06-10 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_rename_name1_tishki_name_tishki_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tishki',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tishki',
            name='size',
            field=models.CharField(default='oversize (xs - xl)', max_length=100),
        ),
    ]
