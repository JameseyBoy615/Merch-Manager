from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse('merch-detail', kwargs={'item_id': self.id})
    
class Comment(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.item.description}'
    
    class Meta:
        ordering = ['-created_at']


