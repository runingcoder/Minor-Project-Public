# Generated by Django 3.2.6 on 2022-03-20 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0005_auto_20220311_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='TriedPass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField()),
                ('username', models.CharField(max_length=200)),
                ('attempted_password', models.CharField(max_length=200)),
            ],
        ),
    ]
