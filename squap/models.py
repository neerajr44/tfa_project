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
            help_text=_('sighting Longitude'),
            max_digits=20,
            decimal_places=15,
            blank = True,
        )

    Y = models.DecimalField(
            help_text=_('sighting Latitude'),
            max_digits =20,
            decimal_places = 15,
            blank = True,
        )


    Shift = models.CharField(
            help_text=_('Which time of the day was squirrel seen - Morning (AM) or Evening (PM)'),
            max_length=10,
            choices=TIME_CHOICES,
            blank = True,
        )
    Date = models.IntegerField(
            help_text=_('Date of sighting'),
            null = True,
            blank = True,
        )

    Unique_squirrel_ID = models.CharField(
            help_text=_('Concatenation of Hectare(after deleting starting 0s) + Shift + first four digits of Date + Hectare squirrel number (after adding 0 in the beginning)'),
            max_length=20,
            primary_key = True,
        )

    Age = models.CharField(
            help_text=_('Was it  Adult or Juvenile'),
            max_length=15,
            choices=AGE_CHOICES,
            blank=True,
        )

    Primary_Fur_Color = models.CharField(
            help_text=_('Choose among gray, cinnamon or black'),
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
            help_text=_('Was it loccated on ground plane or above ground'),
            choices = LOCATION,
            blank = True,
            max_length = 20,
        )

    Specific_Location = models.CharField(
            help_text=_('Any additional comments on the squirrel location?'),
            blank = True,
            max_length = 100,
        )

    Running = models.BooleanField(
            help_text=_('Was squirrel seen running; Then True'),
            default=False,
        )

    Chasing = models.BooleanField(
            help_text=_('Was squirrel seen chasing; Then True'),
            default=False,
         )
    Climbing = models.BooleanField(
            help_text=_('Was squirrel seen climbing; Then True'),
            default=False,
        )
    Eating = models.BooleanField(
            help_text=_('Was squirrel seen Eating; Then True'),
            default=False,
        )

    Foraging = models.BooleanField(
            help_text=_('Was Squirrel seen  Foraging; Then True'),
            default=False,
        )

    Other_Activities = models.CharField(
            help_text=_('Activity the Squirrel was performing'),
            blank=True,
            max_length = 100,
        )

    Kuks = models.BooleanField(
            help_text=_('Was Squirrel seen kuking with a chirpy voice; if no then False'),
            default=False,
        )


    Quaas = models.BooleanField(
            help_text=_('Was Squirrel seen Quaaing,an elongated vocal call; if no then False'),
            default=False,
        )

    Moans = models.BooleanField(
            help_text=_('Was Squirrel seen Moaning,a high pitched voice; if no then False'),
            default=False,
        )

    Tail_flags = models.BooleanField(
            help_text=_('Was Squirrel seen flagging its tail; if no then False'),
            default=False,
        )

    Tail_twitching = models.BooleanField(
            help_text=_('Was Squirrel seen twitching its tail; if no then False'),
            default=False,
        )

    Approaches = models.BooleanField(
        help_text=_('Was Squirrel seen approaching human;if no then False'),
        default=False,
        )

    Indifferent = models.BooleanField(
            help_text=_('Was squirrel indifferent to Human; if no then False'),
            default=False,
        )
    Runs_from = models.BooleanField(
            help_text=_('Was Squirrel seen running from humans; if no then False'),
            default=False,
        )

    def __str__(self):
        return self.Unique_squirrel_ID




# Create your models here.
