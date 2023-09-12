from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", views.home, name="home"),
    path('citizencontractors/', CitizenContractorListView.as_view(),
         name='citizencontractor-list'),
    path('open-international/', OpenInternationalListView.as_view(),
         name='open-international-list'),
    path('open-national/', OpenNationalListView.as_view(),
         name='open-national-list'),
    path('reserved-pwd/', ReservedPWDListView.as_view(), name='reserved-pwd-list'),
    path('reserved-women/', ReservedWomenListView.as_view(),
         name='reserved-women-list'),
    path('reserved-youth/', ReservedYouthListView.as_view(),
         name='reserved-youth-list'),
    path('closed-tenders/', closed_tenders_view, name='closed-tenders'),
    path('closed-awarded-tenders/', views.closed_awarded_tenders_view, name='closed_awarded_tenders'),
    path('supplier_reg/', register_supplier, name='supplier_reg'),
    path('procument/', procurement, name='procurement'),
    path('tenders/', tenders, name='tenders'),
]

