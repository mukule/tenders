from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.utils import timezone
from django.db.models import Q

# Create your views here.


def home(request):
    return render(request, 'main/home.html')


class CitizenContractorListView(ListView):
    model = CitizenContractor
    template_name = 'main/citizencontractor_list.html' 
    context_object_name = 'citizencontractors'

    def get_queryset(self):
        current_datetime = timezone.now()
        queryset = super().get_queryset()
        queryset = queryset.filter(
            opening_date__lte=current_datetime,
            closing_date__gt=current_datetime
        ).order_by('closing_date')
        return queryset


    
class OpenInternationalListView(ListView):
    model = OpenInternational
    template_name = 'main/open_international_list.html'
    context_object_name = 'open_internationals'

    def get_queryset(self):
        current_datetime = timezone.now()
        queryset = super().get_queryset()
        queryset = queryset.filter(
            opening_date__lte=current_datetime,
            closing_date__gt=current_datetime
        ).order_by('closing_date')
        return queryset


class OpenNationalListView(ListView):
    model = OpenNational
    template_name = 'main/open_national_list.html'
    context_object_name = 'open_nationals'

    def get_queryset(self):
        current_datetime = timezone.now()
        queryset = super().get_queryset()
        queryset = queryset.filter(
            opening_date__lte=current_datetime,
            closing_date__gt=current_datetime
        ).order_by('closing_date')
        return queryset


class ReservedPWDListView(ListView):
    model = ReservedPWD
    template_name = 'main/reserved_pwd_list.html'
    context_object_name = 'reserved_pwds'

    def get_queryset(self):
        current_datetime = timezone.now()
        queryset = super().get_queryset()
        queryset = queryset.filter(
            opening_date__lte=current_datetime,
            closing_date__gt=current_datetime
        ).order_by('closing_date')
        return queryset


class ReservedWomenListView(ListView):
    model = ReservedWomen
    template_name = 'main/reserved_women_list.html'
    context_object_name = 'reserved_women'

    def get_queryset(self):
        current_datetime = timezone.now()
        queryset = super().get_queryset()
        queryset = queryset.filter(
            opening_date__lte=current_datetime,
            closing_date__gt=current_datetime
        ).order_by('closing_date')
        return queryset


class ReservedYouthListView(ListView):
    model = ReservedYouth
    template_name = 'main/reserved_youth_list.html'
    context_object_name = 'reserved_youths'

    def get_queryset(self):
        current_datetime = timezone.now()
        queryset = super().get_queryset()
        queryset = queryset.filter(
            opening_date__lte=current_datetime,
            closing_date__gt=current_datetime
        ).order_by('closing_date')
        return queryset
    

class ClosedTendersListView(ListView):
    template_name = 'main/closed_tenders_list.html'
    context_object_name = 'closed_tenders'

    def get_queryset(self):
        current_datetime = timezone.now()

        # Combine the queries from all the models using Q objects
        queryset = CitizenContractor.objects.filter(
            Q(opening_date__lte=current_datetime) & Q(closing_date__lt=current_datetime)
        )
        queryset |= OpenInternational.objects.filter(
            Q(opening_date__lte=current_datetime) & Q(closing_date__lt=current_datetime)
        )
        queryset |= OpenNational.objects.filter(
            Q(opening_date__lte=current_datetime) & Q(closing_date__lt=current_datetime)
        )
        queryset |= ReservedPWD.objects.filter(
            Q(opening_date__lte=current_datetime) & Q(closing_date__lt=current_datetime)
        )
        queryset |= ReservedWomen.objects.filter(
            Q(opening_date__lte=current_datetime) & Q(closing_date__lt=current_datetime)
        )
        queryset |= ReservedYouth.objects.filter(
            Q(opening_date__lte=current_datetime) & Q(closing_date__lt=current_datetime)
        )

        return queryset

