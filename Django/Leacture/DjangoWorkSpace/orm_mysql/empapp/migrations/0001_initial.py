# Generated by Django 4.0.4 on 2022-06-18 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='EmpQuali',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=30)),
                ('hsc', models.IntegerField()),
                ('ssc', models.IntegerField()),
                ('grad', models.IntegerField()),
                ('description', models.TextField(max_length=400)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empapp.emp')),
            ],
            options={
                'db_table': 'emp_qualif',
            },
        ),
    ]
