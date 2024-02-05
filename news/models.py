from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status=self.model.Status.Published)




class Category(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name


class News(models.Model):

    class Status(models.TextChoices):
        Draft="DF","Draft"
        Published="PB","Published"

    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="news_images/")
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    uptade_at=models.DateTimeField(auto_now=True)
    publish_time=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=2,choices=Status.choices,default=Status.Draft)


    object=models.Manager()
    publish=PublishedManager()

    def __str__(self):
        return self.title


class Meta:
    ordering = ["-published_time"]



class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    new=models.ForeignKey(News,on_delete=models.CASCADE)
    body=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)


