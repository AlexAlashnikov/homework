# Generated by Django 4.1.5 on 2023-01-10 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField()),
                ('category_title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=6)),
                ('login', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=150)),
                ('register_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date_created', models.DateField(auto_now=True)),
                ('content', models.CharField(max_length=140)),
                ('post_author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information_service.users')),
                ('post_category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='information_service.category')),
            ],
        ),
    ]
