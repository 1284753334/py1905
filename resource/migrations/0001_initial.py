# Generated by Django 3.0 on 2020-06-15 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 't_sun',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=21)),
            ],
            options={
                'db_table': 't_Teacher',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=32)),
                ('tel', models.CharField(max_length=11)),
                ('Email', models.EmailField(max_length=254)),
                ('sex', models.CharField(choices=[('1', '男'), ('2', '女')], max_length=2)),
                ('birth', models.DateField()),
            ],
            options={
                'db_table': 't_user',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=21)),
                ('sta', models.ManyToManyField(to='resource.Teacher')),
            ],
            options={
                'db_table': 't_student',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourceName', models.CharField(max_length=32)),
                ('resourceType', models.CharField(choices=[('1', '文本文件'), ('2', '电子文件'), ('3', '压缩文件')], max_length=50)),
                ('keywords', models.CharField(max_length=100)),
                ('Socre', models.IntegerField()),
                ('resourceDesc', models.TextField(null=True)),
                ('resourceTime', models.DateTimeField()),
                ('resourceSize', models.IntegerField()),
                ('resource', models.FileField(upload_to='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resource.User')),
            ],
            options={
                'db_table': 't_resource',
            },
        ),
        migrations.CreateModel(
            name='Moon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4)),
                ('sun', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='resource.Sun')),
            ],
            options={
                'db_table': 't_moon',
            },
        ),
    ]