from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Item

# class Item:
#     def __init__(self, item_number, name, department, qty, ):
#         self.item_number = item_number
#         self.name = name
#         self.department = department
#         self.qty = qty

# items = [
#     Item('101010', 'Frz Bagel', '63', '60'),
#     Item('34567', 'Frz shrimp', '63', '88'),
#     Item('234563456', 'Rib eye', '61', '7'),
#     Item('34563456', 'LG tv', '17', '12'),
#     Item('34523432', 'yogurt', '19', '120'),
# ]

class ItemCreate(CreateView):
    model = Item
    fields = ['item_number', 'description', 'department', 'qty', 'exp_date', 'location', 'notes']       

def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def merch_index(request):
    items = Item.objects.all()
    return render(request, 'merch/index.html', {'items': items})

def merch_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'merch/detail.html', {'item': item})