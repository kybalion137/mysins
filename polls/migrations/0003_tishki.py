# Generated by Django 4.2 on 2023-06-10 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_person_goal_person_tg_person_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tishki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
            ],
        ),
    ]
