from django.core.management.base import BaseCommand

import csv
  
from squap.models import Squirrel

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    def handle(self, *args, **options):
        op_dict = {}
        squirrel_list = Squirrel.objects.all()
        with open(options['csv_file'],"w") as fp:
            for item in squirrel_list:
                op_dict['X'] = item.X
                op_dict['Y'] = item.Y
                op_dict['Shift'] = item.Shift
                op_dict['Date'] = item.Date
                op_dict['Unique Squirrel ID'] = item.Unique_squirrel_ID
                op_dict['Age'] = item.Age
                op_dict['Primary Fur Color'] = item.Primary_Fur_Color
                op_dict['Location'] = item.Location
                op_dict['Specific Location'] = item.Specific_Location
                op_dict['Running'] = item.Running
                op_dict['Chasing'] = item.Chasing
                op_dict['Climbing'] = item.Climbing
                op_dict['Eating'] = item.Eating
                op_dict['Foraging'] = item.Foraging
                op_dict['Other Activities'] = item.Other_Activities
                op_dict['Kuks'] = item.Kuks
                op_dict['Quaas'] = item.Quaas
                op_dict['Moans'] = item.Moans
                op_dict['Tail Flags'] = item.Tail_flags
                op_dict['Tail Twitches'] = item.Tail_twitching
                op_dict['Approaches'] = item.Approaches
                op_dict['Indifferent'] = item.Indifferent
                op_dict['Runs from'] = item.Runs_from
                op = csv.DictWriter(fp,delimiter=",",fieldnames=op_dict.keys())
                op.writeheader()
                op.writerow(op_dict)
