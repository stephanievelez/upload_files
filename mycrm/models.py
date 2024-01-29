from django.db import models

# Create your models here.
class NewFile(models.Model):
    upload = models.FileField(upload_to="uploads/")
    # file = models.FileField(upload_to='uploads/')
    #alternatively upload = models.FileField(upload_to="uploads/%Y/%m/%d/")
    name = models.CharField(max_length=70)
    description = models.CharField(blank=True, max_length=70)

    # def __str__(self):
    #     return self.name