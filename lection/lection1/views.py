from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Clienti, Mendgeri, Tarifini_plan, Podchenie_nomera, JurnalSoversheniZvonkov
from .forms import ClientiForm, MendgeriForm, Tarifini_planForm, Podchenie_nomeraForm, JurnalSoversheniZvonkovForm

def Index(requets):
    return render(requets, 'Index.html')

def About(requets):
    return render(requets, 'About.html')

def Contacts(requets):
    return render(requets, 'Contacts.html')

def Location(requets):
    return render(requets, 'Location.html')

def Tariffs(requets):
    return render(requets, 'Tariffs.html')

class ClientiListView(ListView):
    model = Clienti
    template_name = 'clienti_list.html'

class ClientiDetailView(DetailView):
    model = Clienti
    template_name = 'clienti_detail.html'

class ClientiCreateView(CreateView):
    model = Clienti
    form_class = ClientiForm
    template_name = 'clienti_form.html'
    success_url = reverse_lazy('clienti_list')

class ClientiUpdateView(UpdateView):
    model = Clienti
    form_class = ClientiForm
    template_name = 'clienti_form.html'
    success_url = reverse_lazy('clienti_list')

class ClientiDeleteView(DeleteView):
    model = Clienti
    template_name = 'clienti_confirm_delete.html'
    success_url = reverse_lazy('clienti_list')

class MendgeriListView(ListView):
    model = Mendgeri
    template_name = 'mendgeri_list.html'

class MendgeriDetailView(DetailView):
    model = Mendgeri
    template_name = 'mendgeri_detail.html'

class MendgeriCreateView(CreateView):
    model = Mendgeri
    form_class = MendgeriForm
    template_name = 'mendgeri_form.html'
    success_url = reverse_lazy('mendgeri_list')

class MendgeriUpdateView(UpdateView):
    model = Mendgeri
    form_class = MendgeriForm
    template_name = 'mendgeri_form.html'
    success_url = reverse_lazy('mendgeri_list')

class MendgeriDeleteView(DeleteView):
    model = Mendgeri
    template_name = 'mendgeri_confirm_delete.html'
    success_url = reverse_lazy('mendgeri_list')

class Tarifini_planListView(ListView):
    model = Tarifini_plan
    template_name = 'tarif_list.html'

class Tarifini_planDetailView(DetailView):
    model = Tarifini_plan
    template_name = 'tarif_detail.html'

class Tarifini_planCreateView(CreateView):
    model = Tarifini_plan
    form_class = Tarifini_planForm
    template_name = 'tarif_form.html'
    success_url = reverse_lazy('tarif_list')

class Tarifini_planUpdateView(UpdateView):
    model = Tarifini_plan
    form_class = Tarifini_planForm
    template_name = 'tarif_form.html'
    success_url = reverse_lazy('tarif_list')

class Tarifini_planDeleteView(DeleteView):
    model = Tarifini_plan
    template_name = 'tarif_confirm_delete.html'
    success_url = reverse_lazy('tarif_list')

class Podchenie_nomeraListView(ListView):
    model = Podchenie_nomera
    template_name = 'podchenie_list.html'

class Podchenie_nomeraDetailView(DetailView):
    model = Podchenie_nomera
    template_name = 'podchenie_detail.html'

class Podchenie_nomeraCreateView(CreateView):
    model = Podchenie_nomera
    form_class = Podchenie_nomeraForm
    template_name = 'podchenie_form.html'
    success_url = reverse_lazy('podchenie_list')

class Podchenie_nomeraUpdateView(UpdateView):
    model = Podchenie_nomera
    form_class = Podchenie_nomeraForm
    template_name = 'podchenie_form.html'
    success_url = reverse_lazy('podchenie_list')

class Podchenie_nomeraDeleteView(DeleteView):
    model = Podchenie_nomera
    template_name = 'podchenie_confirm_delete.html'
    success_url = reverse_lazy('podchenie_list')

class JurnalListView(ListView):
    model = JurnalSoversheniZvonkov
    template_name = 'jurnal_list.html'

class JurnalDetailView(DetailView):
    model = JurnalSoversheniZvonkov
    template_name = 'jurnal_detail.html'

class JurnalCreateView(CreateView):
    model = JurnalSoversheniZvonkov
    form_class = JurnalSoversheniZvonkovForm
    template_name = 'jurnal_form.html'
    success_url = reverse_lazy('jurnal_list')

class JurnalUpdateView(UpdateView):
    model = JurnalSoversheniZvonkov
    form_class = JurnalSoversheniZvonkovForm
    template_name = 'jurnal_form.html'
    success_url = reverse_lazy('jurnal_list')

class JurnalDeleteView(DeleteView):
    model = JurnalSoversheniZvonkov
    template_name = 'jurnal_confirm_delete.html'
    success_url = reverse_lazy('jurnal_list')