from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    super_user = models.BooleanField(default=False)
    email = models.EmailField(max_length=150, blank=True, null=True) 
    mobile = models.CharField(max_length=15, blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.name} {self.surname} ({self.username})"

class Hours(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    come_in = models.DateTimeField()
    come_out = models.DateTimeField(blank=True, null=True)
    hour = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
