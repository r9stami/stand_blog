from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from account.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE , related_name='posts')
    category = models.ManyToManyField(Category, related_name='posts')
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/posts',null=True, blank=True)
    slug = models.SlugField(unique=True)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        return super(Post ,self).save(*args , **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug':self.slug})


class Comment(models.Model):
    parent = models.ForeignKey('self', null=True,blank=True, on_delete=models.CASCADE, related_name='subs')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title