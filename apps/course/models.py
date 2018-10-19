from django.db import models

class Validator(models.Manager):
    def validation(self, form):
        errors = {}
        if (len(form['name']) < 5):
            errors['name'] = "Name should have more than 4 characters"
        if (len(form['description']) < 15):
            errors['description'] = "Description should have more than 14 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = Validator() 

class Description(models.Model):
    description = models.CharField(max_length=255)
    course = models.OneToOneField(Course, related_name = "description")
