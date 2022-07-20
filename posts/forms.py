from django import forms
from .models import Post
from cloudinary.forms import CloudinaryFileField 
from django.forms import ModelForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


#class PostDirectForm(forms.ModelForm):
 # class Meta:
  #    model = Post
  #image = CloudinaryJsFileField()


# class PhotoForm(ModelForm):
#   class Meta:
#       model = Photo
#       fields = ('image',)
#   image = CloudinaryFileField()

#class edit(ModelForm):
 #   class Meta:
  #      model = Edit
   #     fields = ('content')