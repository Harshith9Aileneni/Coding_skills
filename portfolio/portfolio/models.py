from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length =20)
    number=models.CharField(max_length = 10)
    email=models.EmailField()
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.email}"
