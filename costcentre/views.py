from core.utils import today_string
from core.views import FAdminFilteredView

from django.contrib.auth.mixins import LoginRequiredMixin

from .filters import CostCentreFilter, CostCentreHistoricalFilter
from .tables import CostCentreTable, HistoricalCostCentreTable


class FilteredCostListView(LoginRequiredMixin, FAdminFilteredView):
    table_class = CostCentreTable
    model = table_class.Meta.model
    filterset_class = CostCentreFilter
    name = 'Cost Centre Hierarchy'
    export_name = name + today_string()
    sheet_name = name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_name'] = self.name
        context[
            'section_description'] = 'This field reflects our organisational ' \
                                     'structure which enables ' \
                                     'us to report and produce Financial MI. ' \
                                     'A cost centre is an ' \
                                     'identifiable unit of an organisation whose managers ' \
                                     '(usually Deputy Director or above) ' \
                                     'are responsible for all ' \
                                     'its associated costs and for ensuring adherence to budgets.'
        return context


class FilteredCostHistoricalListView(LoginRequiredMixin, FAdminFilteredView):
    table_class = HistoricalCostCentreTable
    model = table_class.Meta.model
    name = 'Cost Centre Hierarchy 2018-19'
    filterset_class = CostCentreHistoricalFilter
    export_name = name + today_string()
    sheet_name = name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_name'] = self.name
        context[
            'section_description'] = 'Cost Centre Hierarchy for 2018-19'
        return context
