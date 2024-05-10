from typing import Any
from django.db import models
from django.contrib.auth.models import User, AbstractUser

import string
from random import sample


class CodeGenerate(models.Model):
    code = models.CharField(max_length=100, blank=True, unique=True)

    def generate_code():
        return ''.join(sample(string.ascii_letters + string.digits, 13))
    
    @staticmethod
    def save(self, *args, **kwargs):
        if not self.id:
            while True:
                code = self.generate_code()
                if not self.__class__.objects.filter(code=code).count():
                    self.code = code
                    break
        super(CodeGenerate, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class UserProfile(CodeGenerate):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='user/avatar', blank=True, null=True)
    phone = models.CharField(max_length=40, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)


class Group(CodeGenerate):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class GroupUsers(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('group', 'user')


class GroupJoinRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    StatusChoices = [
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=StatusChoices)
    requested_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.text}"