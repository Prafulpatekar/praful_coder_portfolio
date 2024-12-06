from django.db import models
import uuid

# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=300,null=True,blank=True)
    email = models.EmailField(max_length=300,null=True,blank=True)
    subject = models.CharField(max_length=400,null=True,blank=True)
    message = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return f"Message send by {self.name} with email id {self.email}"

class RoleNameModel(models.Model):
    roleName = models.CharField(max_length=50,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return f"{self.roleName}"
    class Meta:
        ordering = ['roleName']

class AboutSectionTitleModel(models.Model):
    titleName = models.CharField(max_length=50,null=True,blank=True)
    value = models.CharField(max_length=500,null=True,blank=True)
    rank = models.PositiveSmallIntegerField(default=1,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return f"{self.titleName}"
    class Meta:
        ordering = ['rank']


class ShortIntroModel(models.Model):
    introText = models.TextField(null=True,blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return f"{self.introText}"
    class Meta:
        ordering = ['-is_active']

class ResumeCounterModel(models.Model):
    counterTitle = models.CharField(max_length=50,null=True,blank=True)
    value = models.PositiveSmallIntegerField(default=1,null=True,blank=True)
    rank = models.PositiveSmallIntegerField(default=1,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return f"{self.titleName}"
    class Meta:
        ordering = ['-created_at']

class MediaFileUploadModel(models.Model):
    fileName = models.CharField(max_length=50,null=True,blank=True)
    buttonTitle = models.CharField(max_length=50,null=True,blank=True)
    actualFile = models.FileField(null=True,blank=True)
    is_downloadable = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return f"{self.titleName}"
    class Meta:
        ordering = ['-created_at']