# Generated by Django 4.2 on 2023-06-10 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_tishki'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tishki',
            old_name='name1',
            new_name='name',
        ),
        migrations.AddField(
            model_name='tishki',
            name='photo',
            field=models.URLField(default=''),
        ),
    ]
