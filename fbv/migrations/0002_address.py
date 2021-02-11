# Generated by Django 3.1.3 on 2021-02-05 05:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('pin', models.IntegerField(validators=[django.core.validators.MinValueValidator(111111), django.core.validators.MaxValueValidator(999999)])),
            ],
        ),
    ]