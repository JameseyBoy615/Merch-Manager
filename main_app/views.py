from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item
from .forms import CommentForm

class Home(LoginView):
    template_name = 'home.html'

class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['item_number', 'description', 'department', 'qty', 'exp_date', 'location', 'notes']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
       
class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['item_number', 'description', 'department', 'qty', 'exp_date', 'location', 'notes' ]

class ItemDelete(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = '/merch/'

@login_required
def merch_index(request):
    items = Item.objects.all()
    return render(request, 'merch/index.html', {'items': items})

@login_required
def user_merch_index(request):
    items = Item.objects.filter(user=request.user)
    return render(request, 'merch/index.html', { 'items': items })

@login_required
def merch_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    comment_form = CommentForm()
    return render(request, 'merch/detail.html', {'item': item, 'comment_form': comment_form})

@login_required
def add_comment(request, item_id):
    
    form = CommentForm(request.POST)
    
    if form.is_valid():
        comment = form.save(commit=False)
        comment.item_id = item_id 
        comment.user = request.user 
        comment.save()

        item = Item.objects.get(id=item_id)
        item.save()
    return redirect('merch-detail', item_id=item_id)
 
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            
            user = form.save()
            
            login(request, user)
            return redirect('merch-index')
        else:
            error_message = 'Invalid sign up - try again'
    
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)