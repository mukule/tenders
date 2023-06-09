from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views.generic import ListView
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.


def home(request):
    return render(request, 'main/home.html')


class CitizenContractorListView(ListView):
    model = CitizenContractor
    template_name = 'main/citizencontractor_list.html'
    context_object_name = 'citizencontractors'

    def get_queryset(self):
        query = self.request.GET.get('query')
        current_datetime = timezone.now()
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(
                Q(tender_title__icontains=query) | Q(
                    tender_ref__icontains=query),
                opening_date__lte=current_datetime,
                closing_date__gt=current_datetime
            ).order_by('closing_date')
        else:
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
        query = self.request.GET.get('query')
        current_datetime = timezone.now()
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(
                Q(tender_title__icontains=query) | Q(
                    tender_ref__icontains=query),
                opening_date__lte=current_datetime,
                closing_date__gt=current_datetime
            ).order_by('closing_date')
        else:
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
        query = self.request.GET.get('query')
        current_datetime = timezone.now()
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(
                Q(tender_title__icontains=query) | Q(
                    tender_ref__icontains=query),
                opening_date__lte=current_datetime,
                closing_date__gt=current_datetime
            ).order_by('closing_date')
        else:
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
        query = self.request.GET.get('query')
        current_datetime = timezone.now()
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(
                Q(tender_title__icontains=query) | Q(
                    tender_ref__icontains=query),
                opening_date__lte=current_datetime,
                closing_date__gt=current_datetime
            ).order_by('closing_date')
        else:
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
        query = self.request.GET.get('query')
        current_datetime = timezone.now()
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(
                Q(tender_title__icontains=query) | Q(tender_ref__icontains=query),
                opening_date__lte=current_datetime,
                closing_date__gt=current_datetime
            ).order_by('closing_date')
        else:
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
        query = self.request.GET.get('query')
        current_datetime = timezone.now()
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(
                Q(tender_title__icontains=query) | Q(tender_ref__icontains=query),
                opening_date__lte=current_datetime,
                closing_date__gt=current_datetime
            ).order_by('closing_date')
        else:
            queryset = queryset.filter(
                opening_date__lte=current_datetime,
                closing_date__gt=current_datetime
            ).order_by('closing_date')

        return queryset
    
def closed_tenders_view(request):
    current_time = timezone.now()

    citizen_contractor_tenders = CitizenContractor.objects.filter(
        closing_date__lte=current_time)
    open_international_tenders = OpenInternational.objects.filter(
        closing_date__lte=current_time)
    open_national_tenders = OpenNational.objects.filter(
        closing_date__lte=current_time)
    reserved_pwd_tenders = ReservedPWD.objects.filter(
        closing_date__lte=current_time)
    reserved_women_tenders = ReservedWomen.objects.filter(
        closing_date__lte=current_time)
    reserved_youth_tenders = ReservedYouth.objects.filter(
        closing_date__lte=current_time)

    query = request.GET.get('query')
    if query:
        citizen_contractor_tenders = citizen_contractor_tenders.filter(
            Q(tender_title__icontains=query) | Q(tender_ref__icontains=query)
        )
        open_international_tenders = open_international_tenders.filter(
            Q(tender_title__icontains=query) | Q(tender_ref__icontains=query)
        )
        open_national_tenders = open_national_tenders.filter(
            Q(tender_title__icontains=query) | Q(tender_ref__icontains=query)
        )
        reserved_pwd_tenders = reserved_pwd_tenders.filter(
            Q(tender_title__icontains=query) | Q(tender_ref__icontains=query)
        )
        reserved_women_tenders = reserved_women_tenders.filter(
            Q(tender_title__icontains=query) | Q(tender_ref__icontains=query)
        )
        reserved_youth_tenders = reserved_youth_tenders.filter(
            Q(tender_title__icontains=query) | Q(tender_ref__icontains=query)
        )

    all_closed_tenders = list(citizen_contractor_tenders) + \
        list(open_international_tenders) + \
        list(open_national_tenders) + \
        list(reserved_pwd_tenders) + \
        list(reserved_women_tenders) + \
        list(reserved_youth_tenders)

    paginator = Paginator(all_closed_tenders, 5)  # Display 5 tenders per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
    }

    return render(request, 'main/closed_tenders_list.html', context)

def closed_awarded_tenders_view(request):
    current_time = timezone.now()

    citizen_contractor_tenders = CitizenContractor.objects.filter(closing_date__lte=current_time, awarded_status=True)
    open_international_tenders = OpenInternational.objects.filter(closing_date__lte=current_time, awarded_status=True)
    open_national_tenders = OpenNational.objects.filter(closing_date__lte=current_time, awarded_status=True)
    reserved_pwd_tenders = ReservedPWD.objects.filter(closing_date__lte=current_time, awarded_status=True)
    reserved_women_tenders = ReservedWomen.objects.filter(closing_date__lte=current_time, awarded_status=True)
    reserved_youth_tenders = ReservedYouth.objects.filter(closing_date__lte=current_time, awarded_status=True)

    query = request.GET.get('query')
    if query:
        citizen_contractor_tenders = citizen_contractor_tenders.filter(
            Q(tender_title__icontains=query) | Q(tender_ref__icontains=query)
        )
        open_international_tenders = open_international_tenders.filter(
            Q(tender_title__icontains=query) | Q(tender_ref__icontains=query)
        )
        open_national_tenders = open_national_tenders.filter(
            Q(tender_title__icontains=query) | Q(tender_ref__icontains=query)
        )
        reserved_pwd_tenders = reserved_pwd_tenders.filter(
            Q(tender_title__icontains=query) | Q(tender_ref__icontains=query)
        )
        reserved_women_tenders = reserved_women_tenders.filter(
            Q(tender_title__icontains=query) | Q(tender_ref__icontains=query)
        )
        reserved_youth_tenders = reserved_youth_tenders.filter(
            Q(tender_title__icontains=query) | Q(tender_ref__icontains=query)
        )

    all_closed_tenders = list(citizen_contractor_tenders) + \
                         list(open_international_tenders) + \
                         list(open_national_tenders) + \
                         list(reserved_pwd_tenders) + \
                         list(reserved_women_tenders) + \
                         list(reserved_youth_tenders)

    paginator = Paginator(all_closed_tenders, 5)  # Display 5 tenders per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
    }

    return render(request, 'main/closed_awarded_tenders_list.html', context)

def register_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_registration_success')  # Redirect to a success page
    else:
        form = SupplierForm()
    
    return render(request, 'main/supplier_registration.html', {'form': form})
