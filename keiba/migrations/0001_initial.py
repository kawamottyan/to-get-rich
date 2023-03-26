# Generated by Django 4.1.7 on 2023-03-21 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_number', models.FloatField()),
                ('horse_number', models.FloatField()),
                ('horse_weight', models.FloatField()),
                ('distance', models.FloatField()),
                ('rank', models.FloatField()),
            ],
        ),
    ]
