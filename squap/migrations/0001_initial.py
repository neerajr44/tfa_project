# Generated by Django 3.0 on 2019-12-06 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('X', models.DecimalField(blank=True, decimal_places=15, help_text='Longitutde of sighting', max_digits=20)),
                ('Y', models.DecimalField(blank=True, decimal_places=15, help_text='Latitude of sighting', max_digits=20)),
                ('Shift', models.CharField(blank=True, choices=[('AM', 'AM'), ('PM', 'PM')], help_text='Indication whether the sighting occurred in the afterrnoon or evening', max_length=10)),
                ('Date', models.IntegerField(blank=True, help_text='Date of the sighting', null=True)),
                ('Unique_squirrel_ID', models.CharField(help_text='Concatenation of Hectare(after deleting starting 0s) + Shift + first four digits of Date + Hectare squirrel number (after adding 0 in the beginning)', max_length=20, primary_key=True, serialize=False)),
                ('Age', models.CharField(blank=True, choices=[('ADULT', 'ADULT'), ('JUVENILE', 'JUVENILE')], help_text='Value is either Adult or Juvenile', max_length=15)),
                ('Primary_Fur_Color', models.CharField(blank=True, choices=[('GRAY', 'GRAY'), ('CINAMMON', 'CINNAMON'), ('BLACK', 'BLACK')], help_text='Value is either gray, cinnamon or black', max_length=10)),
                ('Location', models.CharField(blank=True, choices=[('GROUND PLANE', 'GROUND PlANE'), ('ABOVE GROUND', 'ABOVE GROUND')], help_text='Either ground plane or above ground depending on where the sighters located the squirrel', max_length=20)),
                ('Specific_Location', models.CharField(blank=True, help_text='Additional commentary on the squirrel location', max_length=100)),
                ('Running', models.BooleanField(default=False, help_text='True if squirrel seen running; otherwise False')),
                ('Chasing', models.BooleanField(default=False, help_text='True if squirrel was seen chasing;otherwise False')),
                ('Climbing', models.BooleanField(default=False, help_text='True if Squirrel was seen climbing;otherwise False')),
                ('Eating', models.BooleanField(default=False, help_text='True if Squirrel is Eating; otherwise False')),
                ('Foraging', models.BooleanField(default=False, help_text='True if Squirrel is Foraging; otherwise False')),
                ('Other_Activities', models.CharField(blank=True, help_text='Activity the Squirrel is performing', max_length=100)),
                ('Kuks', models.BooleanField(default=False, help_text='True if the Squirrel is kuking,a chirpy voice communication; otherwise False')),
                ('Quaas', models.BooleanField(default=False, help_text='True if the Squirrel is Quaaing,an elongated vocal call; otherwise False')),
                ('Moans', models.BooleanField(default=False, help_text='True if the Squirrel is Moaning,a high pitched vocal communication; otherwise False')),
                ('Tail_flags', models.BooleanField(default=False, help_text='True if the Squirrel is flagging its tail; otherwise False')),
                ('Tail_twitching', models.BooleanField(default=False, help_text='True if the Squirrel is twitching its tail; otherwise False')),
                ('Approaches', models.BooleanField(default=False, help_text='True if the Squirrel is seen approaching human;otherwise False')),
                ('Indifferent', models.BooleanField(default=False, help_text='True if squirrel was indifferent to Human; otherwise False')),
                ('Runs_from', models.BooleanField(default=False, help_text='True if Squirrel was seen running from humans; otherwise false')),
            ],
        ),
    ]
