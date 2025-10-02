from django.db import models
from django.utils import timezone


# Biography Model
class Biography(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    profile_image = models.ImageField(upload_to='profiles/')
    phone = models.CharField(max_length=20, blank=True)
    

    def __str__(self):
        return self.name


# Service Model
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.title


# Logos Model
class Logos(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.name


# Project Model
class Project(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(max_length=200, blank=True)
    github_link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    position = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    challenge_name = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()  # Percentage from 0 to 100

    def __str__(self):
        return self.name


# Mails Model
class Email(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=False)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email


class AboutWork(models.Model):
    title = models.CharField(max_length=200)
    number = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class ExtraText(models.Model):
    text = models.TextField()
    icon = models.CharField(max_length=100)  # You can store icon class names or paths_

    def __str__(self):
        return self.text[:50]  # Return first 50 characters for representation


class HeadingText(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
    
class SuccessStory(models.Model):
    success_count = models.IntegerField()
    success_description = models.CharField(max_length=100)

class SocialLink(models.Model):
    platform = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    icon = models.CharField(max_length=100)  # You can store icon class names or paths

    def __str__(self):
        return self.platform