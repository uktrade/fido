from django.urls import path

from forecast.views.edit_forecast import (
    AddRowView,
    ChooseCostCentreView,
    EditForecastFigureView,
    EditForecastView,
    EditUnavailableView,
    ErrorView,
    PasteForecastRowsView,
    SlowView,
)
from forecast.views.export.mi_report_source import (
    export_mi_budget_report,
    export_mi_report,
)
from forecast.views.export.oscar_return import export_oscar_report
from forecast.views.upload_file import (
    UploadActualsView,
    UploadBudgetView,
)
from forecast.views.view_forecast.expenditure_details import (
    CostCentreExpenditureDetailsView,
    DITExpenditureDetailsView,
    DirectorateExpenditureDetailsView,
    GroupExpenditureDetailsView,
)
from forecast.views.view_forecast.export_forecast_data import (
    export_edit_forecast_data,
    export_forecast_data_cost_centre,
    export_forecast_data_directorate,
    export_forecast_data_dit,
    export_forecast_data_expenditure_detail_cost_centre,
    export_forecast_data_expenditure_detail_directorate,
    export_forecast_data_expenditure_detail_group,
    export_forecast_data_expenditure_dit,
    export_forecast_data_group,
    export_forecast_data_programme_detail_directorate,
    export_forecast_data_programme_detail_dit,
    export_forecast_data_programme_detail_group,
    export_forecast_data_project_detail_cost_centre,
    export_forecast_data_project_detail_directorate,
    export_forecast_data_project_detail_dit,
    export_forecast_data_project_detail_group,
)
from forecast.views.view_forecast.forecast_summary import (
    CostCentreView,
    DITView,
    DirectorateView,
    GroupView,
)
from forecast.views.view_forecast.programme_details import (
    DITProgrammeDetailsView,
    DirectorateProgrammeDetailsView,
    GroupProgrammeDetailsView,
)
from forecast.views.view_forecast.project_details import (
    CostCentreProjectDetailsView,
    DITProjectDetailsView,
    DirectorateProjectDetailsView,
    GroupProjectDetailsView,
)


urlpatterns = [
    path("slow/", SlowView.as_view(), name="slow"),
    path("error/", ErrorView.as_view(), name="error"),
    path(
        "edit/<int:cost_centre_code>/", EditForecastView.as_view(), name="edit_forecast"
    ),
    path(
        "edit/editing-unavailable/",
        EditUnavailableView.as_view(),
        name="edit_unavailable",
    ),
    path(
        "edit/add/<int:cost_centre_code>/",
        AddRowView.as_view(),
        name="add_forecast_row",
    ),
    path(
        "edit/choose-cost-centre/",
        ChooseCostCentreView.as_view(),
        name="choose_cost_centre",
    ),
    path("view/dit/<int:period>/", DITView.as_view(), name="forecast_dit",),
    path(
        "view/group/<group_code>/<int:period>/",
        GroupView.as_view(),
        name="forecast_group",
    ),
    path(
        "view/directorate/<directorate_code>/<int:period>/",
        DirectorateView.as_view(),
        name="forecast_directorate",
    ),
    path(
        "view/cost-centre/<cost_centre_code>/",
        CostCentreView.as_view(),
        name="forecast_cost_centre",
    ),
    path(
        "view/cost-centre/<cost_centre_code>/<int:period>/",
        CostCentreView.as_view(),
        name="forecast_cost_centre",
    ),
    path(
        "view/dit/<expenditure_category>/<budget_type>/<int:period>/",
        DITExpenditureDetailsView.as_view(),
        name="expenditure_details_dit",
    ),
    path(
        "view/group/<group_code>/<expenditure_category>/<budget_type>/<int:period>/",
        GroupExpenditureDetailsView.as_view(),
        name="expenditure_details_group",
    ),
    path(
        "view/directorate/<directorate_code>/<expenditure_category>/<budget_type>/<int:period>/",  # noqa
        DirectorateExpenditureDetailsView.as_view(),
        name="expenditure_details_directorate",
    ),
    path(
        "view/cost-centre/<cost_centre_code>/<expenditure_category>/<budget_type>/<int:period>/",   # noqa
        CostCentreExpenditureDetailsView.as_view(),
        name="expenditure_details_cost_centre",
    ),
    #         dit-programme/310530/6/
    path(
        "view/dit-programme/<programme_code>/<forecast_expenditure_type>/<int:period>/",
        DITProgrammeDetailsView.as_view(),
        name="programme_details_dit",
    ),
    #  group-programme/1090HT/310530/6/
    path(
        "view/group-programme/<group_code>/<programme_code>/<forecast_expenditure_type>/<int:period>/",  # noqa
        GroupProgrammeDetailsView.as_view(),
        name="programme_details_group",
    ),
    #  directorate-programme/10907T/310530/6/
    path(
        "view/directorate-programme/<directorate_code>/<programme_code>/<forecast_expenditure_type>/<int:period>/",  # noqa
        DirectorateProgrammeDetailsView.as_view(),
        name="programme_details_directorate",
    ),
    path(
        "dit-project/<project_code>/<int:period>/",
        DITProjectDetailsView.as_view(),
        name="project_details_dit",
    ),
    path(
        "group-project/<group_code>/<project_code>/<int:period>/",
        GroupProjectDetailsView.as_view(),
        name="project_details_group",
    ),
    #  directorate-project/10907T/310530/6/
    path(
        "directorate-project/<directorate_code>/<project_code>/<int:period>/",
        DirectorateProjectDetailsView.as_view(),
        name="project_details_directorate",
    ),
    #  directorate-project/10907T/310530/6/
    path(
        "cost-centre_project/<cost_centre_code>/<project_code>/<int:period>/",
        CostCentreProjectDetailsView.as_view(),
        name="project_details_costcentre",
    ),
    path("upload-actuals/", UploadActualsView.as_view(), name="upload_actuals_file"),
    path("upload-budgets/", UploadBudgetView.as_view(), name="upload_budget_file"),
    path(
        "paste-forecast/<cost_centre_code>/",
        PasteForecastRowsView.as_view(),
        name="paste_forecast",
    ),
    path(
        "update-forecast/<cost_centre_code>/",
        EditForecastFigureView.as_view(),
        name="update_forecast_figure",
    ),
    path(
        "export-forecast-data/dit/<int:period>",
        export_forecast_data_dit,
        name="export_forecast_data_dit",
    ),
    path(
        "export-forecast-data/group/<group_code>/<int:period>",
        export_forecast_data_group,
        name="export_forecast_data_group",
    ),
    path(
        "export-forecast-data/directorate/<directorate_code>/<int:period>",
        export_forecast_data_directorate,
        name="export_forecast_data_directorate",
    ),
    path(
        "export-forecast-data/cost-centre/<cost_centre>/<int:period>",
        export_forecast_data_cost_centre,
        name="export_forecast_data_cost_centre",
    ),
    path(
        "export-edit-forecast-data/<cost_centre>",
        export_edit_forecast_data,
        name="export_edit_forecast_data_cost_centre",
    ),
    path("download_oscar/", export_oscar_report, name="download_oscar"),
    path(
        "download_mi_report_source/", export_mi_report, name="download_mi_report_source"
    ),
    path("download_mi_budget/", export_mi_budget_report, name="download_mi_budget"),
    path(
        "export-expenditure-details/dit/<expenditure_category_id>/<budget_type_id>/<int:period>", # noqa
        export_forecast_data_expenditure_dit,
        name="export_expenditure_details_dit",
    ),
    path(
        "export-expenditure-details/group/<group_code>/<expenditure_category_id>/<budget_type_id>/<int:period>",  # noqa
        export_forecast_data_expenditure_detail_group,
        name="export_expenditure_details_group",
    ),
    path(
        "export-expenditure-details/directorate/<directorate_code>/<expenditure_category_id>/<budget_type_id>/<int:period>",  # noqa
        export_forecast_data_expenditure_detail_directorate,
        name="export_expenditure_details_directorate",
    ),
    path(
        "export-expenditure-details/cost-centre/<cost_centre>/<expenditure_category_id>/<budget_type_id>/<int:period>",  # noqa
        export_forecast_data_expenditure_detail_cost_centre,
        name="export_expenditure_details_cost_centre",
    ),
    path(
        "export-project-details/cost-centre/<cost_centre>/<project_code_id>/<int:period>", # noqa
        export_forecast_data_project_detail_cost_centre,
        name="export_forecast_data_project_detail_cost_centre",
    ),
    path(
        "export-project-details/directorate/<directorate_code>/<project_code_id>/<int:period>", # noqa
        export_forecast_data_project_detail_directorate,
        name="export_forecast_data_project_detail_directorate",
    ),
    path(
        "export-project-details/group/<group_code>/<project_code_id>/<int:period>",
        export_forecast_data_project_detail_group,
        name="export_forecast_data_project_detail_group",
    ),
    path(
        "export-project-details/<project_code_id>/<int:period>",
        export_forecast_data_project_detail_dit,
        name="export_forecast_data_project_detail_dit",
    ),
    path(
        "export-dit-programme/<programme_code_id>/<forecast_expenditure_type_name>/<int:period>", # noqa
        export_forecast_data_programme_detail_dit,
        name="export_programme_details_dit",
    ),
    path(
        "export-group-programme/<group_code>/<programme_code_id>/<forecast_expenditure_type_name>/<int:period>",  # noqa
        export_forecast_data_programme_detail_group,
        name="export_programme_details_group",
    ),
    path(
        "export-directorate-programme/<directorate_code>/<programme_code_id>/<forecast_expenditure_type_name>/<int:period>",  # noqa
        export_forecast_data_programme_detail_directorate,
        name="export_programme_details_directorate",
    ),
]
