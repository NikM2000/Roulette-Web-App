# Generated by Django 2.2 on 2019-04-20 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinoapp', '0006_auto_20190420_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
            ],
        ),
    ]