from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
def validate_img(upload): 
      ext = upload.name[-4:]
      if not ext in ['.jpg', ".png"]:
        raise ValidationError(u'File type not supported!')    
      if upload.size > 1024*500:
        raise ValidationError(u'File too big!')    
class Branch(models.Model):
    name = models.CharField(max_length=50)
    hod = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Notice(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    attachment1=models.FileField(upload_to = "doc\\", null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    def __str__(self):
        return self.subject

class Student(models.Model):
    name = models.CharField(max_length=200, null=True)
    skills = models.TextField(null=True) 
    sem = models.IntegerField(default=1, validators=[MaxValueValidator(8), MinValueValidator(1)])
    marks_10 = models.FloatField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])    
    marks_12 = models.FloatField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])    
    marks_aggr = models.FloatField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])    
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    myimg=models.ImageField(upload_to = "images\\", validators=[validate_img], null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name   
