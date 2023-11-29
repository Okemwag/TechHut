from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50,verbose_name='Projects',
                            null=False)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.name
