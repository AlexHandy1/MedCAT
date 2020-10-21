# Generated by Django 3.1 on 2020-10-21 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConceptDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('cdb_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='VocabDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('vocab_file', models.FileField(upload_to='')),
            ],
        ),
    ]