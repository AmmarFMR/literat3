# from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User

# # Create your models here.
# class Posts(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     created_at = models.DateTimeField(default=timezone.now, blank=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, default=404)
    
#     def __str__(self):
#         return self.title
        
#     class Meta:
#         verbose_name_plural = "Posts"

from django.db import models
from datetime import datetime

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name_plural = "Posts"
