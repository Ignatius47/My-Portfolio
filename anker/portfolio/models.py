from django.db import models

class HomeSection(models.Model):
    greeting = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    hire_me_text = models.CharField(max_length=50)
    my_works_text = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.title}"


class Developer(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    bio = models.TextField()  # Short description about yourself
    profile_image = models.ImageField(upload_to='profile_images/')  # Profile picture
    projects_completed = models.IntegerField(default=0)  # Number of completed projects
    cv = models.FileField(upload_to='cvs/', null=True, blank=True)  # CV upload

    def __str__(self):
        return self.name
    
class Resume(models.Model):
    bio = models.TextField()  # Bio or general info
    cv = models.FileField(upload_to='resumes/', null=True, blank=True)  # CV file

    def __str__(self):
        return "Resume"

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True) 

    def __str__(self):
        return self.name

from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField() 
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

class ContactInfo(models.Model):
    contact_type = models.CharField(max_length=50)
    value = models.CharField(max_length=200) 
    icon = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.contact_type

class Counter(models.Model):
    label = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self):
        return self.label

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f'Message from {self.name}'
