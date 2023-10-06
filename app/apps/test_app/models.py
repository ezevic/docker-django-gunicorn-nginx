from django.db import models

# Create your models here.


class TestModel(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
