from company.views import Views as CompanyViews
from catalog.views import Views as CatalogViews

class ViewFactory:
    @staticmethod
    def get_company_views():
        return CompanyViews()

    @staticmethod
    def get_catalog_views():
        return CatalogViews()
