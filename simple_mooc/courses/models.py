from django.db import models


class Course(models.Model):
    name = models.CharField('courses name', max_length=30)
    slug = models.SlugField('shortcut')
    description = models.TextField('description', blank=True)
    start_date = models.DateField('start date', null=True, blank=True)
    image = models.ImageField(
        upload_to='courses/images',
        verbose_name='Image',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField('last modified', auto_now=True)
