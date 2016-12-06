from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseBadRequest, JsonResponse
from django.core.urlresolvers import reverse_lazy

import json

from .models import Papermail, Tag
from .forms import PapermailUpdateForm

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

class PapermailList(ListView):
    
    model = Papermail
    context_object_name = 'files'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        
        context = super(FichierList, self).get_context_data(**kwargs)

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
        
        queryset = Papermail.objects.all().filter(propriete_de=self.request.user)
        
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
    
    model = Papermail
    fields = ['paper_file','name_file','sender','recipient','date_paper','tag','property_of']
    template_name = 'paperworks/papermail_create_form.html'
    
    def get_initial(self):
        
        initial = super(PapermailCreate, self).get_initial()
        
        initial['property_of'] = self.request.user
        
        return initial
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PapermailCreate, self).dispatch(*args, **kwargs)

class PapermailUpdate(AjaxableResponseMixin, UpdateView):
    
    model = Papermail
    form_class = PapermailUpdateForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PapermailUpdate, self).dispatch(*args, **kwargs)
    
class PapermailDelete(AjaxableResponseMixin, DeleteView):
    model = Papermail
    success_url = reverse_lazy('papermail-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PapermailDelete, self).dispatch(*args, **kwargs)