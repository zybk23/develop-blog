from django.db import models
from  django.conf import settings
from django.template.defaultfilters import slugify
from PIL import Image

# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=250)
    slug=models.SlugField()

    def __str__(self):
        return self.title
    def save(self,*args,**kwargs) :
       self.slug=slugify(self.title)
       super(Category,self).save(*args,**kwargs)
    def post_count(self):
        return self.counts.all().count()


class Post(models.Model):
    title=models.CharField(max_length=150)
    content=models.TextField()
    publishing_date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(blank=True,null=True,upload_to="uploads/")
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    slug=models.SlugField()
    slider_post=models.BooleanField(default=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1,related_name="counts")
    hit=models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):

        self.slug=slugify(self.title)
        super(Post,self).save(*args,**kwargs)
    def comment_count(self):
        return self.comments.all().count()    
    
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    content=models.TextField()
    publishing_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.post.title
        