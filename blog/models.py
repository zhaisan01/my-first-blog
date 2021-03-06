from django.conf import settings 
from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text=CKEditor5Field('Text', config_name='extends')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    
    def __str__(self):
        return self.title