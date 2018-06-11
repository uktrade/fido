from django.core.management.base import BaseCommand, CommandError
from core.csvimport.costcentre import  import_cc
from core.csvimport.treasurysegment import import_treasury_segments
from core.csvimport.programme import import_programme
from core.csvimport.treasuryCOA import import_treasury_COA
from core.csvimport.nac import import_NAC
from core.csvimport.actual import import_actual
from core.csvimport.analysis import import_Analysis1, import_Analysis2

import csv

IMPORT_TYPE = {
    'CostCentre': import_cc,
    'Segments' : import_treasury_segments,
    'COAs': import_treasury_COA,
    'Programmes': import_programme,
    'NAC':import_NAC,
    'Analysis1': import_Analysis1,
    'Analysis2': import_Analysis2,
}

class Command(BaseCommand):
    help = 'Import CC hierarchy from csv file'

    def add_arguments(self, parser):
        parser.add_argument('csv_path')
        parser.add_argument('type')
        parser.add_argument('year', type=int, nargs='?', default=None)
        parser.add_argument('month',  nargs='?', default=None)
# pass the file path as an argument
# second argument will define the content of the file
# importing actual is a special case, because we need to specify the month
    def handle(self, *args, **options):
        path = options.get('csv_path')
        importtype = options.get('type')
        csvfile = open(path, newline='', encoding='cp1252')  # Windows-1252 or CP-1252, used because of a back quote
        if importtype == 'Actuals':
            financialyear = options.get('year')
            print (financialyear)
            monthtoimport = options.get('month')
            print(monthtoimport)
            import_actual(csvfile, financialyear, monthtoimport)
        else:
            IMPORT_TYPE[importtype](csvfile)
        csvfile.close()






