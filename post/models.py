from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length = 120)
    content = RichTextField()
    publishing_date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(null = True, blank = True)
    slug = models.SlugField(unique = True, editable = False, max_length = 130)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug': self.slug})

    def get_create_url(self):
        return reverse('post:create')
    
    def get_update_url(self):
        return reverse('post:update', kwargs={'slug': self.slug})
    
    def get_delete_url(self):
        return reverse('post:delete', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug = unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['-publishing_date', 'id']

class Comment(models.Model):
    name = models.CharField(max_length = 200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    post = models.ForeignKey('post.Post', related_name = 'comments', on_delete = models.CASCADE)