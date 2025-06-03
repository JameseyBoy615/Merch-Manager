from django.db import models
from django.urls import reverse

class Item(models.Model):
    item_number = models.IntegerField()
    description = models.CharField(max_length=100)
    department = models.IntegerField()
    qty = models.IntegerField()
    exp_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100)
    notes = models.CharField(max_length=250)
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse('merch-detail', kwargs={'item_id': self.id})
    


