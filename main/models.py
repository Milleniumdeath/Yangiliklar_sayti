from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PublishedManager(models.Model):
    def get_queryset(self):
        return super().get_queryset().filter(published=True)

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    intro = models.TextField()
    image = models.ImageField(upload_to='articles')
    author = models.CharField(max_length=255)
    reading_time = models.DurationField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    published = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    category =models.ForeignKey(Category, on_delete=models.CASCADE)
    tags =models.ManyToManyField(Tag)

    objects = models.Manager()
    published_objects = PublishedManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            base_slug = slugify(self.title)
            unique_slug = base_slug

            counter = 1
            while Article.objects.filter(slug=unique_slug).exists():
                base_slug = f"{unique_slug}-{counter}"
                counter += 1
            self.slug = base_slug
            super().save(*args, **kwargs)

class Content(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text =models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=f'contents/', blank=True, null=True)

    def __str__(self):
        return f"{self.article.title}'s  content"
    def save(self, *args, **kwargs):
        if not self.text and  not self.image:
            raise ValidationError("Rasm yoki matn kiritilishi shart")
        super().save(*args, **kwargs)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="Anonymous")
    email = models.EmailField(max_length=32, blank=True, null=True)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}'s comment"

class Newslatter(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email

class Moment(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='moments')
    author = models.CharField(max_length=255)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    seen = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.phone and not self.email:
            raise ValidationError("Telefon raqam yoki emailingizni kiriting")
        super().save(*args, **kwargs)

