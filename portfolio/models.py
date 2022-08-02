from django.db import models

# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=300,null=True,blank=True)
    email = models.EmailField(max_length=300,null=True,blank=True)
    subject = models.CharField(max_length=400,null=True,blank=True)
    message = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Message send by {self.name} with email id {self.email}"