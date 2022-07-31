from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class InfoAbout(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=80)
    content = RichTextField()
    image = models.ImageField(upload_to="moments")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    order = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ["order","title"]

    def __str__(self):
        return self.title
    



