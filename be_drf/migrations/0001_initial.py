# Generated by Django 4.1.1 on 2022-10-02 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('nick_name', models.CharField(max_length=50)),
                ('email', models.EmailField(default=None, max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=20)),
            ],
        ),

        migrations.CreateModel(
            name='Indicacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description2', models.TextField()),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
    ]
