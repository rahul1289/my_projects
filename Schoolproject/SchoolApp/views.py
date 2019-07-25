from django.shortcuts import render
from django.urls import reverse_lazy

from . import models
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    print("heloooooooooooooo")
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context  = super(IndexView,self).get_context_data(**kwargs)
        context['injectme'] = "Hai user here is your template view!"
        return context


class SchoolListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'

    # Example of making your own:
    # context_object_name = 'schools'
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.School
    template_name = 'SchoolApp/school_detail.html'



class SchoolCreateView(CreateView):
    fields = ("name","principal","location")
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ("name","principal")
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("SchoolApp:list")

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("SchoolApp:list")


# Create your views here.
