from django.db import models

# Create your models here.
class URLShortenModel(models.Model):
    name=models.CharField(max_length=20)
    long_url=models.CharField(max_length=500)
    short_url=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name