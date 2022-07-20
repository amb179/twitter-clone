from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse

class Post(models.Model):
    class Meta(object):
        db_table = 'posts'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )
    body = models.CharField(
        'Body', blank=True, null=True, max_length=140, db_index=True
    )
    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )
    likes = models.IntegerField(
        'likes', default=0, blank=True
    )
    #edit = models.CharField(
     #   'Edit', blank=True, null=True, max_length=None
    #)
    
    
    image = CloudinaryField(
        'Image', blank=True, db_index=True
    )


#from django.db import models
#from cloudinary.models import CloudinaryField

# class Photo(models.Model):
#     image = CloudinaryField('image', null=True, blank=True)