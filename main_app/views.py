from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Item

class ItemCreate(CreateView):
    model = Item
    fields = ['item_number', 'description', 'department', 'qty', 'exp_date', 'location', 'notes']
       
class ItemUpdate(UpdateView):
    model = Item
    fields = ['item_number', 'description', 'department', 'qty', 'exp_date', 'location', 'notes' ]

class ItemDelete(DeleteView):
    model = Item
    success_url = '/merch/'

def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def merch_index(request):
    items = Item.objects.all()
    return render(request, 'merch/index.html', {'items': items})

def merch_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'merch/detail.html', {'item': item})