from django.urls import path
from utils.view_factory import ViewFactory

company_views = ViewFactory.get_company_views()

urlpatterns = [
    path('about/', company_views.about, name='about'),
]