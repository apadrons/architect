from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100,default='Empty')
    image = models.ImageField(upload_to="uploads/")
    description = models.CharField(max_length=250,default='')
    
    def __str__(self) -> str:
        return self.title