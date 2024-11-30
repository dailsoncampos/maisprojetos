from django.urls import path
from utils.view_factory import ViewFactory

catalog_views = ViewFactory.get_catalog_views()

urlpatterns = [
    path('', catalog_views.catalog, name='catalog'),
]
