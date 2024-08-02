from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    password = models.CharField(max_length=50)
    superuser = models.BooleanField(default=False)
    email = models.EmailField(max_length=150, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Hours(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    come_in = models.DateTimeField()
    come_out = models.DateTimeField(null=True, blank=True)
    hours = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.come_in} to {self.come_out}"
