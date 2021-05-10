from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    TF = models.BooleanField()
    email = models.EmailField()
    URL = models.URLField()
    like = models.PositiveIntegerField()

    def __str__(self):
        return self.title

