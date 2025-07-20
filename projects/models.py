from django.db import models

class Project(models.Model):
    title       = models.CharField(max_length=200)
    link        = models.URLField(blank=True)
    year        = models.PositiveIntegerField()
    branch      = models.CharField(max_length=100)
    PROJECT_TYPES = [
        ("web", "Web"),
        ("ml",  "Machine Learning"),
        ("ai",  "AI/ML"),
        ("db",  "Database"),
    ]
    project_type = models.CharField(max_length=10, choices=PROJECT_TYPES)

    def __str__(self):
        return f"{self.title} ({self.year})"
