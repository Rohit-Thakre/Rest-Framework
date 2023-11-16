from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    
    name = models.CharField(max_length=50)
    CEO = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=(('IT', 'IT'), 
                                     ('Non IT', 'Non IT')
                                     ))
    about = models.TextField()
    base = models.CharField(max_length=50)
    active = models.BooleanField(default=1)

    created = models.DateTimeField(auto_now_add= True)
    by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def __unicode__(self):
        return 
