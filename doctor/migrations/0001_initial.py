# Generated by Django 3.1.4 on 2020-12-19 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('speciality', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeslot', models.IntegerField(choices=[(0, '09:00-10:00'), (1, '10:00-11:00'), (2, '11:00-12:00'), (3, '12:00-13:00'), (4, '13:00-14:00'), (5, '14:00-15:00'), (6, '15:00-16:00'), (7, '16:00-17:00')])),
                ('date', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.patient')),
            ],
            options={
                'unique_together': {('patient', 'date', 'timeslot')},
            },
        ),
    ]