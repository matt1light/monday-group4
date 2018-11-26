# Generated by Django 2.1.2 on 2018-11-25 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainModels', '0006_auto_20181119_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking_start', models.DateTimeField()),
                ('parking_end', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='spot',
            name='last_park',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='parkingevent',
            name='spot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parking_events', to='mainModels.Spot'),
        ),
    ]