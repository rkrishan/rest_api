# Generated by Django 2.1.2 on 2018-10-19 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=20)),
                ('companyName', models.CharField(blank=True, default='', max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zip', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('web', models.URLField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]