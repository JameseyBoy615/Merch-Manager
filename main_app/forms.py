from django import forms
from .models import Comment
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['description', 'item_number', 'department', 'qty', 'exp_date', 'location', 'notes', 'is_resolved']
        widgets = {
            'description': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-md p-2 '
            }),
            'item_number': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-md p-2'
            }),
            'department': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-md p-2'
            }),
            'qty': forms.NumberInput(attrs={
                'class': 'w-full border border-gray-300 rounded-md p-2'
            }),
            'exp_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full border border-gray-300 rounded-md p-2'
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-md p-2'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-md p-2',
                'rows': 3
            }),
            'is_resolved': forms.CheckboxInput(attrs={
                'class': 'mr-2'
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 4,
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm  sm:text-sm'
            }),
        }