from django.db import models

# Create your models here.
class Public(models.Model):
    name=models.CharField(max_length=50)
    picture=models.ImageField(upload_to='img',blank=True,null=True)

    def __str__(self):
        return self.name