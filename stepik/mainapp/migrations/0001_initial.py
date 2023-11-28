# Generated by Django 4.1.7 on 2023-11-25 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(max_length=50)),
                ('russian', models.CharField(max_length=50)),
                ('comments', models.TextField(max_length=250)),
                ('pushed_data', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]