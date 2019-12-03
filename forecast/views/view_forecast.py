from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.shortcuts import (
    render,
    reverse,
)
from django.views.generic.base import TemplateView

from django_tables2 import (
    MultiTableMixin,
    RequestConfig,
    SingleTableView,
)

from core.views import FidoExportMixin

from costcentre.forms import (
    DirectorateCostCentresForm,
)
from costcentre.models import (
    CostCentre,
    Directorate,
)
from costcentre.models import DepartmentalGroup

from forecast.models import (
    MonthlyFigure,
)
from forecast.tables import (
    ForecastSubTotalTable,
    ForecastTable,
)
from forecast.views.base import ForecastViewPermissionMixin
from forecast.views.view_forecast_queries import (
    budget_type_cost_centre_columns,
    budget_type_cost_directorate_columns,
    budget_type_cost_group_columns,
    programme_columns,
    natural_account_columns,
)

TEST_COST_CENTRE = 109076
TEST_FINANCIAL_YEAR = 2019


class PivotClassView(
    ForecastViewPermissionMixin,
    FidoExportMixin,
    SingleTableView,
):
    template_name = "forecast/forecast.html"
    sheet_name = "Forecast"
    filterset_class = None
    table_class = ForecastTable

    table_pagination = False

    def get_table_kwargs(self):
        return {"column_dict": self.column_dict}

    def __init__(self, *args, **kwargs):
        # set the queryset at init, because it
        # requires the current year, so it is
        # recall each time. Maybe an overkill,
        # but I don't want to risk to forget
        # to change the year!
        d1 = {
            "cost_centre__directorate__group": "Group",
            "cost_centre__directorate__group__group_name": "Name",
        }
        q = MonthlyFigure.pivot.pivot_data(d1.keys())
        self.queryset = q
        self.column_dict = d1
        super().__init__(*args, **kwargs)


class CostClassView(
    ForecastViewPermissionMixin,
    FidoExportMixin,
    SingleTableView,
):
    template_name = "forecast/forecast.html"
    sheet_name = "Forecast"
    filterset_class = None
    table_class = ForecastTable
    table_pagination = False

    def get_table_kwargs(self):
        return {"column_dict": self.column_dict}

    def __init__(self, *args, **kwargs):
        # set the queryset at init, because it
        # requires the current year, so it is
        # recall each time. Maybe an overkill,
        # but I don't want to risk to forget
        # to change the year!
        columns = {
            "cost_centre__cost_centre_code": "Cost Centre Code",
            "cost_centre__cost_centre_name": "Cost Centre Description",
            "natural_account_code__natural_account_code": "Natural Account Code",
            "natural_account_code__natural_account_code_description": "Natural Account Code Description",  # noqa
            "programme__programme_code": "Programme Code",
            "programme__programme_description": "Programme Description",
            "project_code__project_code": "Project Code",
            "project_code__project_description": "Project Description",
            "programme__budget_type_fk__budget_type_display": "Budget Type",
            "natural_account_code__expenditure_category__NAC_category__NAC_category_description": "Budget Grouping",  # noqa
            "natural_account_code__expenditure_category__grouping_description": "Budget Category", # noqa
            "natural_account_code__account_L5_code__economic_budget_code": "Expenditure Type", # noqa
        }
        cost_centre_code = TEST_COST_CENTRE
        pivot_filter = {"cost_centre__cost_centre_code": "{}".format(cost_centre_code)}
        q = MonthlyFigure.pivot.pivot_data(columns.keys(), pivot_filter)
        self.queryset = q
        self.column_dict = columns
        super().__init__(*args, **kwargs)




def get_forecast_table():
    # TODO remove hardcoded cost centre
    # TODO the filter will be set from the request

    cost_centre_code = TEST_COST_CENTRE
    order_list = ["programme__budget_type_fk__budget_type_display_order"]
    pivot_filter = {"cost_centre__cost_centre_code": "{}".format(cost_centre_code)}

    sub_total_type = ["programme__budget_type_fk__budget_type_display"]
    display_sub_total_column = "cost_centre__cost_centre_name"
    q1 = MonthlyFigure.pivot.subtotal_data(
        display_sub_total_column,
        sub_total_type,
        budget_type_cost_centre_columns.keys(),
        pivot_filter,
        order_list=order_list,
    )

    # subtotal_data
    order_list_prog = [
        "programme__budget_type_fk__budget_type_display_order",
        "forecast_expenditure_type__forecast_expenditure_type_display_order",
    ]
    sub_total_prog = [
        "programme__budget_type_fk__budget_type_display",
        "forecast_expenditure_type__forecast_expenditure_type_description",
    ]
    display_sub_total_column = "programme__programme_description"

    q2 = MonthlyFigure.pivot.subtotal_data(
        display_sub_total_column,
        sub_total_prog,
        programme_columns.keys(),
        pivot_filter,
        order_list=order_list_prog,
    )

    sub_total_nac = [
        "programme__budget_type_fk__budget_type_display",
        "natural_account_code__expenditure_category__NAC_category__NAC_category_description",  # noqa
    ]
    display_sub_total_column = (
        "natural_account_code__expenditure_category__grouping_description"
    )
    order_list_nac = [
        "programme__budget_type_fk__budget_type_display_order",
        "natural_account_code__expenditure_category__NAC_category__NAC_category_description",  # noqa
    ]

    q3 = MonthlyFigure.pivot.subtotal_data(
        display_sub_total_column,
        sub_total_nac,
        natural_account_columns.keys(),
        pivot_filter,
        order_list=order_list_nac,
    )
    return [
        ForecastSubTotalTable(budget_type_cost_centre_columns, q1),
        ForecastSubTotalTable(programme_columns, q2),
        ForecastSubTotalTable(natural_account_columns, q3),
    ]


class MultiForecastView(
    ForecastViewPermissionMixin,
    MultiTableMixin,
    TemplateView,
):
    template_name = "forecast/forecastmulti.html"

    # table_pagination = {
    #     'per_page': 30
    # }
    table_pagination = False

    def __init__(self, *args, **kwargs):
        self.tables = get_forecast_table()
        super().__init__(*args, **kwargs)


def pivot_test1(request):
    order_list_hierarchy = ["programme__budget_type_fk__budget_type_display_order"]

    sub_total_type = ["programme__budget_type_fk__budget_type_display"]
    display_sub_total_column_cost_centre = "cost_centre__cost_centre_name"
    directorate_code = 109076
    pivot_filter = {"cost_centre__directorate__directorate_code": f"{directorate_code}"}
    hierarchy_data = MonthlyFigure.pivot.subtotal_data(
        display_sub_total_column_cost_centre,
        sub_total_type,
        budget_type_cost_centre_columns.keys(),
        pivot_filter,
        order_list=order_list_hierarchy,
    )

    table = ForecastSubTotalTable(budget_type_cost_centre_columns, hierarchy_data)
    RequestConfig(request).configure(table)
    return render(request, "forecast/forecast.html", {"table": table})


