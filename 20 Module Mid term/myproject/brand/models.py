from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField(max_length=100, unique=True , null=True, blank=True)

    def __str__(self):
        return self.name
    @staticmethod
    def get_all_brands():
        return Brand.objects.all()

