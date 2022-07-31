from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class ProjectMiniature(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to="projects")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    order = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class Project(models.Model):
    project_miniature = models.ForeignKey(ProjectMiniature, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=80)
    description = RichTextField()
    technologies = models.CharField(max_length=200)
    client = models.CharField(max_length=100)
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    url = models.URLField(null=True, blank=True)
    repo = models.URLField(null=True, blank=True)



    def __str__(self):
        return self.project_name
    



