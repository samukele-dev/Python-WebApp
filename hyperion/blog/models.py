from django.db import models

# Create your models here.


class Post(models.Model):
    # Default behaviour - Django creates primary keys
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()


def _str_(self):
    return self.title
