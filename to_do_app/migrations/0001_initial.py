# Generated by Django 3.0.2 on 2020-02-01 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
