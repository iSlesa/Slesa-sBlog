from django.db import models
from django.core.urlresolvers import reverse
#import Pillow

CATEGORIES = (('personal','personal'),
('designing','designing'),
('programming','programming')
)

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length = 255)
    #category = models.CharField(max_length = 50)
    category = models.CharField(max_length = 50, choices = CATEGORIES)
    content = models.TextField()
    published = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to = 'images', null=True, blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])
