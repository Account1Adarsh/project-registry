
# Create your models here.
from django.db import models

class Project(models.Model):
    MAJOR_MINOR = [
        ('minor', 'Minor'),
        ('major', 'Major'),
    ]

    title      = models.CharField(max_length=200)
    link       = models.URLField(help_text="GitHub/Live demo URL")
    year       = models.PositiveIntegerField()
    batch      = models.CharField(max_length=20, help_text="e.g. ’2021–25’")
    branch     = models.CharField(max_length=100, help_text="e.g. Computer Science")
    project_type = models.CharField(max_length=5, choices=MAJOR_MINOR)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.year}, {self.project_type})"
