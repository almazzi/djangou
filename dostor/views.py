from django.shortcuts import render
from django.views.generic import *
from dostor.models import Dostor
from django.core.urlresolvers import reverse
from dostor.forms import DostorForm

class DostorListView(ListView):
    model = Dostor
    template_name = 'dostor_list.html'


class DostorCreateView(CreateView):
    model = Dostor
    template_name = 'dostor_edit.html'
    form_class = DostorForm


    def get_success_url(self):
        return reverse('dos-list')

    def get_context_data(self, **kwargs):
        context = super(DostorCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('dos-create')
        return context

class DostorUpdateView(UpdateView):
    model = Dostor
    template_name = 'dostor_edit.html'
    form_class = DostorForm

    def get_success_url(self):
        return reverse('dos-list')

    def get_context_data(self, **kwargs):
        context = super(DostorUpdateView,self).get_context_data(**kwargs)
        context['action'] = reverse('dos-edit', kwargs={'pk':self.get_object().id})
        return context


class DostorDeleteView(DeleteView):
    model = Dostor
    template_name = 'dostor_delete.html'

    def get_success_url(self):
        return reverse('dos-list')

class DostorDetailView(DetailView):
    model = Dostor
    template_name = 'dostor_detail.html'



# Create your views here.
