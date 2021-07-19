# Generated by Django 3.2.5 on 2021-07-19 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnrollmentProjection',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('course_code', models.CharField(max_length=50)),
                ('course_name', models.CharField(max_length=400)),
                ('academic_period', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=400)),
                ('estimated_amount', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'enrollment_projection',
            },
        ),
    ]
