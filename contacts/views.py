from contacts.models import Contact
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse


class ListContactView(ListView):
    model = Contact
    template_name = 'contact_list.html'


class CreateContactView(CreateView):

    model = Contact
    template_name = 'edit_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):

        context = super(CreateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contact-new')
        return context


class UpdateContactView(UpdateView):
    model = Contact
    template_name = 'edit_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):

        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contact-edit', kwargs={'pk': self.get_object().id})
        return context


class DeleteContactView(DeleteView):
    model = Contact
    template_name = 'delete_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')


class DetailContactView(DetailView):
    model = Contact
    template_name = 'detail.html'











# Create your views here.
