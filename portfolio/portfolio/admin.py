from django.contrib import admin
from portfolio.models import Contact

print("DEBUG: admin.py is being loaded!")
admin.site.register(Contact)
print("DEBUG: Contact model registered!")