# Generated by Django 2.1.3 on 2018-11-28 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200, unique=True, verbose_name='URL: ')),
                ('name', models.CharField(max_length=200, verbose_name='Name: ')),
                ('isbn', models.CharField(max_length=500, verbose_name='ISBN: ')),
                ('publisher_year', models.IntegerField(verbose_name='Year of publication: ')),
                ('publisher_name', models.CharField(max_length=300, verbose_name='Publisher: ')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
