from django.shortcuts import render
from django.http import HttpResponse

class Item:
    def __init__(self, item_number, name, department, qty, ):
        self.item_number = item_number
        self.name = name
        self.department = department
        self.qty = qty

items = [
    Item('101010', 'Frz Bagel', '63', '60'),
    Item('34567', 'Frz shrimp', '63', '88'),
    Item('234563456', 'Rib eye', '61', '7'),
    Item('34563456', 'LG tv', '17', '12'),
    Item('34523432', 'yogurt', '19', '120'),
]

        

def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Home Page</h1>')

def merch_index(request):
    return render(request, 'merch/index.html', {'items': items})