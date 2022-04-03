from django.db import models


class Search (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    content_images = models.ImageField(upload_to="photos/Y%/m%/d%")
    time_c = models.DateTimeField(auto_now_add=True)


