from django.db import models

from django.utils.translation import gettext as _

# Create your models here.

class Squirrel(models.Model):


    AM = 'AM'
    PM = 'PM'

    ADULT = 'ADULT'
    JUVENILE = 'JUVENILE'

    Gray = 'GRAY'
    Cinnamon = 'CINAMMON'
    Black = 'BLACK'


    AGE_CHOICES = (
            (ADULT, 'ADULT'),
            (JUVENILE, 'JUVENILE'),
        )

    TIME_CHOICES = (
            (AM, 'AM'),
            (PM, 'PM'),
        )


    COLOR_CHOICES = (
            (Gray, 'GRAY'),
            (Cinnamon, 'CINNAMON'),
            (Black, 'BLACK'),
        )


    X = models.DecimalField(
            help_text=_('Longitutde of sighting'),
            max_digits=20,
            decimal_places=15,
            blank = True,
        )

    Y = models.DecimalField(
            help_text=_('Latitude of sighting'),
            max_digits =20,
            decimal_places = 15,
            blank = True,
        )
    

    Shift = models.CharField(
            help_text=_('Indication whether the sighting occurred in the afterrnoon or evening'),
            max_length=10,
            choices=TIME_CHOICES,
            blank = True,
        )
    Date = models.IntegerField(
            help_text=_('Date of the sighting'),
            null = True,
            blank = True,
        )

    Unique_squirrel_ID = models.CharField(
            help_text=_('Concatenation of Hectare(after deleting starting 0s) + Shift + first four digits of Date + Hectare squirrel number (after adding 0 in the beginning)'),
            max_length=20,
            primary_key = True,
        )

    Age = models.CharField(
            help_text=_('Value is either Adult or Juvenile'),
            max_length=15,
            choices=AGE_CHOICES,
            blank=True,
        )

    Primary_Fur_Color = models.CharField(
            help_text=_('Value is either gray, cinnamon or black'),
            max_length = 10,
            choices = COLOR_CHOICES,
            blank = True,
        )


    GROUND_PLANE = 'GROUND PLANE'
    ABOVE_GROUND = 'ABOVE GROUND'

    LOCATION= (
            (GROUND_PLANE, 'GROUND PlANE'),
            (ABOVE_GROUND, 'ABOVE GROUND'),
        )

    Location = models.CharField(
            help_text=_('Either ground plane or above ground depending on where the sighters located the squirrel'),
            choices = LOCATION,
            blank = True,
            max_length = 20,
        )

    Specific_Location = models.CharField(
            help_text=_('Additional commentary on the squirrel location'),
            blank = True,
            max_length = 100,
        )

    Running = models.BooleanField(
            help_text=_('True if squirrel seen running; otherwise False'),
            default=False,
        )

    Chasing = models.BooleanField(
            help_text=_('True if squirrel was seen chasing;otherwise False'),
            default=False,
         )
    Climbing = models.BooleanField(
            help_text=_('True if Squirrel was seen climbing;otherwise False'),
            default=False,
        )
    Eating = models.BooleanField(
            help_text=_('True if Squirrel is Eating; otherwise False'),
            default=False,
        )
     
    Foraging = models.BooleanField(
            help_text=_('True if Squirrel is Foraging; otherwise False'),
            default=False,
        )
     
    Other_Activities = models.CharField(
            help_text=_('Activity the Squirrel is performing'),
            blank=True,
            max_length = 100,
        )
            
    Kuks = models.BooleanField(
            help_text=_('True if the Squirrel is kuking,a chirpy voice communication; otherwise False'),
            default=False,
        )
    

    Quaas = models.BooleanField(
            help_text=_('True if the Squirrel is Quaaing,an elongated vocal call; otherwise False'),
            default=False,
        )
     
    Moans = models.BooleanField(
            help_text=_('True if the Squirrel is Moaning,a high pitched vocal communication; otherwise False'),
            default=False,
        )
            
    Tail_flags = models.BooleanField(
            help_text=_('True if the Squirrel is flagging its tail; otherwise False'),
            default=False,
        )
            
    Tail_twitching = models.BooleanField(
            help_text=_('True if the Squirrel is twitching its tail; otherwise False'),
            default=False,
        )
            
    Approaches = models.BooleanField(
        help_text=_('True if the Squirrel is seen approaching human;otherwise False'),
        default=False,
        )
            
    Indifferent = models.BooleanField(
            help_text=_('True if squirrel was indifferent to Human; otherwise False'),
            default=False,
        )
    Runs_from = models.BooleanField(
            help_text=_('True if Squirrel was seen running from humans; otherwise false'),
            default=False,
        )

    def __str__(self):
        return self.Unique_squirrel_ID
            


# Create your models here.
