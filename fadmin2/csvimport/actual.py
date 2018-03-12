from core.models import ADIReport as adi, CostCentre as cc

import csv

# define the column position in the csv file.
# it reflects the position of columns in the Orcle report used to download the actuals

__columnKey = {
            'Entity': 1,
            'Cost Centre': 2,
            'Account': 3,
            'Programme': 4,
            'Analysis 1': 5,
            'Analysis 2': 6,
            'April': 7,
            'May': 8,
            'June': 9,
            'July': 10,
            'August': 11,
            'September': 12,
            'October': 13,
            'November': 14,
            'December': 15,
            'January': 16,
            'February': 17}

import datetime from datetime

def financialyear():
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    if currentMonth < 4 : # the new financial year  starts in April
        currentYear = currentYear - 1 # before April, the financial year it is one year behin
    return currentYear
