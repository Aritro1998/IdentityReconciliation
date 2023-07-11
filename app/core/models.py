from django.db import models

# Create your models here.
class Contact(models.Model):
    phoneNumber = models.CharField(max_length=10, null=True, blank=True)
    email = models.CharField(max_length=100,null=True)
    linkedId = models.IntegerField(null=True, editable=False)
    linkChoices = [('primary', 'primary'), ('secondary', 'secondary',)]
    linkPrecedence = models.CharField(max_length=15, choices=linkChoices, default='primary', editable=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    deletedAt = models.DateTimeField(null=True, blank=True, editable=False)