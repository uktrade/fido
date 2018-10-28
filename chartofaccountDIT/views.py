from core.views import FAdminFilteredView

from .filters import Analysis1Filter, Analysis2Filter, \
    CommercialCategoryFilter, ExpenditureCategoryFilter, \
    NACFilter, ProgrammeFilter
from .tables import Analysis1Table, Analysis2Table, \
    CommercialCategoryTable, ExpenditureCategoryTable, \
    NaturalCodeTable, ProgrammeTable


class FilteredNACListView(FAdminFilteredView):
    table_class = NaturalCodeTable
    model = table_class.Meta.model
    filterset_class = NACFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_name'] = 'Natural Account Codes (NAC)'
        context['section_description'] = 'This field tells us what we are spending the money on. ' \
                                         'The structure follows the Treasury Common Chart of ' \
                                         'Accounts and groups a set of transactions ' \
                                         'into a clearly defined category.'
        return context


class FilteredExpenditureCategoryListView(FAdminFilteredView):
    table_class = ExpenditureCategoryTable
    model = table_class.Meta.model
    filterset_class = ExpenditureCategoryFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_name'] = 'Budget Categories'
        context['section_description'] = 'The field helps you in acquiring the correct ' \
                                         'Natural Account Code for your purchase ' \
                                         'from a financial perspective.'
        return context


class FilteredCommercialCategoryListView(FAdminFilteredView):
    table_class = CommercialCategoryTable
    model = table_class.Meta.model
    filterset_class = CommercialCategoryFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_name'] = 'Commercial Categories'
        context['section_description'] = 'The field helps you in acquiring the correct ' \
                                         'Natural Account Code for your purchase ' \
                                         'from a procurement perspective.'
        return context


class FilteredAnalysis1ListView(FAdminFilteredView):
    table_class = Analysis1Table
    model = table_class.Meta.model
    filterset_class = Analysis1Filter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_name'] = 'Contract Reconciliation (Analysis 1)'
        context['section_description'] = 'This field helps to reconcile with Commercial’s unique ' \
                                         'contract identifier. It will enable the organisation ' \
                                         'to match spend on the financial system ' \
                                         'to specific contracts.'
        return context


class FilteredAnalysis2ListView(FAdminFilteredView):
    table_class = Analysis2Table
    model = table_class.Meta.model
    filterset_class = Analysis2Filter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_name'] = 'Markets (Analysis 2)'
        context['section_description'] = 'This field is used by the Overseas Team. ' \
                                         'The cost centre structure  identifies our 9 regions, ' \
                                         'however, within each region ' \
                                         'the spend is needed by country.'
        return context


class FilteredProgrammeView(FAdminFilteredView):
    table_class = ProgrammeTable
    model = table_class.Meta.model
    filterset_class = ProgrammeFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_name'] = 'Programme Codes'
        context['section_description'] = 'This field tells us why we are spending the money ' \
                                         'i.e. what we are trying to deliver on. ' \
                                         'This reflects the two most important reporting ' \
                                         'requirements that DIT is likely to have to HMG over ' \
                                         'the next few years (EU exit and ODA) ' \
                                         'and Parliament Control Total ' \
                                         '(DEL/AME and Admin/Programme).'
        return context
