from django.db import models
from django.utils.timezone import now

class News(models.Model):
    title = models.CharField(max_length=255)
    pre_description = models.CharField(max_length=2000)
    description = models.TextField()
    added_date = models.DateTimeField(default=now, editable=False)  # Updated to DateTimeField
    author = models.CharField(max_length=255, blank=True, null=True)
    author_position = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to='news_photos/', blank=True, null=True)

    def __str__(self):
        return self.title

# Gallery Model
class Gallery(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Photo Model
class Photo(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Connection(models.Model):
    title = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=100)
    email_address = models.EmailField()
    working_hours = models.CharField(max_length=255)
    first_phone = models.CharField(max_length=20)
    second_phone = models.CharField(max_length=20, blank=True, null=True)
    embed_map_html = models.TextField(blank=True, null=True)  # New field for the embed HTML code

    def __str__(self):
        return self.title


class Governance(models.Model):
    position = models.CharField(max_length=255)  # Position of the person
    fullname = models.CharField(max_length=255)  # Full name
    working_hours = models.CharField(max_length=255)  # Working hours (e.g., "9:00 AM - 5:00 PM")
    email_post = models.EmailField()  # Email address
    photo = models.ImageField(upload_to='governance_photos/', blank=True, null=True)  # Photo of the person

    def __str__(self):
        return f"{self.fullname} - {self.position}"


class Resolution(models.Model):
    title = models.CharField(max_length=255)  # Title of the resolution
    link = models.URLField()  # URL link to the resolution document or page

    def __str__(self):
        return self.title

class Provision(models.Model):
    title = models.CharField(max_length=255)  # Title of the provision
    link = models.URLField()  # URL link to the provision document or page

    def __str__(self):
        return self.title