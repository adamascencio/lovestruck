from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Location, Partner, Date
from .forms import DateForm
from datetime import date


# Create your views here.
def home(request):
    dates = Date.objects.all().filter(user=request.user, date=date.today())
    return render(request, 'home.html', {'dates':dates})

def signup(request): 
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class LocationList(ListView):
    model = Location
    fields = ['name', 'category', 'city', 'state']


class LocationCreate(LoginRequiredMixin, CreateView):
    model = Location
    fields = ['name', 'address', 'phone_num', 'city', 'state', 'category']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class LocationDetail(LoginRequiredMixin, DetailView):
    model = Location
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['partner_list'] = Partner.objects.filter(user=self.request.user)
        context['date_form'] = DateForm()
        return context


class LocationUpdate(LoginRequiredMixin, UpdateView):
    model = Location
    fields = ['name', 'address', 'phone_num', 'city', 'state', 'category']


class LocationDelete(LoginRequiredMixin, DeleteView):
    model = Location
    success_url = '/locations/'


class PartnerList(LoginRequiredMixin, ListView):
    model = Partner
    fields = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['partner_list'] = Partner.objects.filter(
            user=self.request.user)
        return context


class PartnerCreate(LoginRequiredMixin, CreateView):
    model = Partner
    fields = ['name', 'notes']
    success_url = '/partners/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PartnerDetail(LoginRequiredMixin, DetailView):
    model = Partner
    fields = '__all__'


class PartnerUpdate(LoginRequiredMixin, UpdateView):
    model = Partner
    fields = ['name', 'notes']


class PartnerDelete(LoginRequiredMixin, DeleteView):
    model = Partner
    success_url = '/partners/'


class DateList(LoginRequiredMixin, ListView):
    model = Date
    fields = ['location', 'partner']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_list'] = Date.objects.filter(
            user=self.request.user)
        return context


class DateCreate(LoginRequiredMixin, CreateView):
    model = Date
    form_class = DateForm

    def form_valid(self, form):
        form.instance.partner_id = self.request.POST.get('partner_id')
        form.instance.location_id = self.request.POST.get('location_id')
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = '/dates/'


class DateDetail(LoginRequiredMixin, DetailView):
    model = Date

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['partner_list'] = Partner.objects.filter(
            user=self.request.user)
        return context

class DateUpdate(LoginRequiredMixin, UpdateView):
    model = Date
    fields = ['activity', 'date', 'budget', 'rating', 'notes']


class DateDelete(LoginRequiredMixin, DeleteView):
    model = Date
    success_url = '/dates/'
