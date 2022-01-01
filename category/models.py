from django.db import models

# Create your models here.
class Category(models.Model):
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    category_name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to="photo/categories", blank=True)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
