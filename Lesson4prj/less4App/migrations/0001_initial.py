# Generated by Django 2.2.3 on 2019-08-03 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Employee Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email Address')),
                ('dob', models.DateTimeField(verbose_name='Date of Birth')),
                ('salary', models.FloatField(verbose_name='Monthly Salary')),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]
