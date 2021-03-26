# Generated by Django 3.0.2 on 2020-03-28 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_event', models.CharField(max_length=100)),
                ('days', models.IntegerField(help_text='Minimum child age in days to be eligible to go to         the event')),
                ('event_date', models.DateField()),
                ('msg', models.TextField()),
            ],
            options={
                'verbose_name': 'Scheduled Event',
            },
        ),
    ]
