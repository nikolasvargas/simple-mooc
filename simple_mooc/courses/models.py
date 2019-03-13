from django.db import models


class CourseManager(models.Manager):
    def search(self, query):
        return super().get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(description__icontains=query)
        )

    def __repr__(self):
        pass

    def __str__(self):
        pass


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
    objects = CourseManager()

    def __str__(self):
        return self.name
