from django.shortcuts import render

# Create your views here.
from pApp.models import Product
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class P_list(ListView):
    model = Product


class P_View(DetailView):
    model = Product

class P_Create(CreateView):
    model = Product
    fields = ['pname', 'price']
    success_url = reverse_lazy('P_list')


class P_Update(UpdateView):
    model = Product
    fields = ['pname', 'price']
    success_url = reverse_lazy('P_list')

class P_Delete(DeleteView):
    model = Product
    success_url = reverse_lazy('P_list')