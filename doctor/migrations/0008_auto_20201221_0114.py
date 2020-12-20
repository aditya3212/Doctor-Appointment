# Generated by Django 3.1.4 on 2020-12-20 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_auto_20201221_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='timeslot',
            field=models.CharField(choices=[('09:00-10:00', '09:00-10:00'), ('10:00-11:00', '10:00-11:00'), ('11:00-12:00', '11:00-12:00'), ('12:00-13:00', '12:00-13:00'), ('13:00-14:00', '13:00-14:00'), ('14:00-15:00', '14:00-15:00'), ('15:00-16:00', '15:00-16:00'), ('16:00-17:00', '16:00-17:00')], max_length=100),
        ),
    ]
