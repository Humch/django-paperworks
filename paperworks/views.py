from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseBadRequest, JsonResponse
from django.core.urlresolvers import reverse_lazy

import json

from .models import Papermail, Tag, Sender, Recipient
from .forms import PapermailForm

# Mixin pour la gestion des formulaires envoyés par AJAX --> issu du site Django https://docs.djangoproject.com/fr/1.9/topics/class-based-views/generic-editing/

class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
                'name_file': self.object.name_file,
            }
            return JsonResponse(data)
        else:
            return response

class SenderAjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(SenderAjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(SenderAjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
                'name': self.object.name,
            }
            return JsonResponse(data)
        else:
            return response

class PapermailList(ListView):
    
    model = Papermail
    context_object_name = 'papermails'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        
        context = super(PapermailList, self).get_context_data(**kwargs)

        context['all_tags'] = Tag.objects.all()
        
        return context
    
    def get_template_names(self, **kwargs):
    
        if self.request.method == 'GET' and self.request.is_ajax():
        
            if self.request.GET.get("action") == "details":
        
                template_name = 'paperworks/papermail_list/details.html'
        
            elif self.request.GET.get("action") == "mosaic":
        
                template_name = 'paperworks/papermail_list/mosaic.html'
            
            elif self.request.GET.get("action") == "list":
        
                template_name = 'paperworks/papermail_list/list.html'
                
            self.request.session['fileview'] = template_name
            
        else:
            template_name = 'paperworks/papermail_list.html'
            
            if not 'fileview' in self.request.session:
                self.request.session['fileview'] = 'paperworks/papermail_list/mosaic.html'
            
        return template_name
    
    def get_queryset(self):
        
        queryset = Papermail.objects.all().filter(property_of=self.request.user)
        
        return queryset

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PapermailList, self).dispatch(*args, **kwargs)
    
class PapermailDetail(DetailView):

    model = Papermail
    
    def get_context_data(self, **kwargs):
        
        context = super(PapermailDetail, self).get_context_data(**kwargs)

        context['all_tags'] = Tag.objects.all()
        
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PapermailDetail, self).dispatch(*args, **kwargs)

class PapermailCreate(AjaxableResponseMixin, CreateView):
    """
    View to create a Papermail. Works with ajax.
    """
    
    model = Papermail
    form_class = PapermailForm
    template_name = 'paperworks/papermail_create_form.html'
    
    def form_valid(self, form):
        form.instance.property_of = self.request.user
        return super(PapermailCreate, self).form_valid(form)
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PapermailCreate, self).dispatch(*args, **kwargs)

class PapermailUpdate(AjaxableResponseMixin, UpdateView):
    """
    View to update a Papermail. Works with ajax.
    Use default template papermail_form.html
    """
    
    model = Papermail
    form_class = PapermailForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PapermailUpdate, self).dispatch(*args, **kwargs)
    
class PapermailDelete(AjaxableResponseMixin, DeleteView):
    """
    View to delete a Papermail. Works with ajax.
    Use default template papermail_confirm_delete.html
    """
    
    model = Papermail
    success_url = reverse_lazy('papermail-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PapermailDelete, self).dispatch(*args, **kwargs)

class SenderCreate(SenderAjaxableResponseMixin,CreateView):
    
    model = Sender
    fields = ['name']
    template_name = 'paperworks/sender_create_form.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SenderCreate, self).dispatch(*args, **kwargs)

class RecipientCreate(SenderAjaxableResponseMixin,CreateView):
    
    model = Recipient
    fields = ['name']
    template_name = 'paperworks/recipient_create_form.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RecipientCreate, self).dispatch(*args, **kwargs)