from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    def can_be_deleted(self):
        return not self.users.exists()


class User(models.Model):
    username = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')

    def __str__(self):
        return self.username
