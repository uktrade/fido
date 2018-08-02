from .models import CostCentre, DepartmentalGroup, Directorate, Programme
from core.myutils import import_obj, IMPORT_CSV_MODEL_KEY, IMPORT_CSV_PK_KEY, IMPORT_CSV_FIELDLIST_KEY


# define the column position in the csv file.

# COLUMN_KEY = {
#                 'GroupCode': 3,
#                 'GroupName': 4,
#                 'DirectorateCode': 5,
#                 'DirectorateName': 6,
#                 'CCCode': 7,
#                 'CCName': 8}
#
#
# def importcostcentres(csvfile):
#     csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
#     for row in csvreader:
#         # Create DG Group, Directorate and Cost centre
#         objDG, created = DepartmentalGroup.objects.update_or_create(
#             GroupCode=row[COLUMN_KEY['GroupCode']],
#             defaults={'GroupName': row[COLUMN_KEY['GroupName']]},
#         )
#         objdir, created = Directorate.objects.update_or_create(
#             DirectorateCode=row[COLUMN_KEY['DirectorateCode']],
#             defaults={'GroupCode': objDG,
#                        'DirectorateName':row[COLUMN_KEY['DirectorateName']]},
#         )
#         obj, created = CostCentre.objects.update_or_create(
#             CCCode=row[COLUMN_KEY['CCCode']],
#             defaults={CostCentre.CCName.field_name: row[COLUMN_KEY['CCName']],
#                       CostCentre.Directorate.field.name: objdir},
#         )
#

GROUP_KEY = {IMPORT_CSV_MODEL_KEY: DepartmentalGroup,
             IMPORT_CSV_PK_KEY: 'GroupCode',
             'fieldlist' : {DepartmentalGroup.group_name.field_name: 'GroupName'}}


DIR_KEY = {IMPORT_CSV_MODEL_KEY: Directorate,
           IMPORT_CSV_PK_KEY: 'DirectorateCode',
           IMPORT_CSV_FIELDLIST_KEY: {Directorate.directorate_name.field_name: 'DirectorateDescription',
                                        Directorate.group.field.name: GROUP_KEY}}

CC_KEY = {IMPORT_CSV_MODEL_KEY: CostCentre,
          IMPORT_CSV_PK_KEY: 'CCCode',
          IMPORT_CSV_FIELDLIST_KEY: {CostCentre.cost_centre_name.field_name: 'CCDescription',
                                        CostCentre.active.field_name: 'Active',
                                        CostCentre.directorate.field.name: DIR_KEY}}


def import_cc(csvfile):
    import_obj(csvfile, CC_KEY)


PROG_KEY = {IMPORT_CSV_MODEL_KEY: Programme,
            IMPORT_CSV_PK_KEY: 'Code',
            IMPORT_CSV_FIELDLIST_KEY: {Programme.programme_description.field_name: 'Description',
                                        Programme.budget_type.field_name: 'Type'}}


def import_programme(csvfile):
    import_obj(csvfile, PROG_KEY)