# Import the Django admin module
from django.contrib import admin

# Import the models you want to register in the admin panel
from .models import JobDescription, Resume  

# Register the Resume model to appear in the Django Admin dashboard
admin.site.register(Resume)

# Register the JobDescription model to appear in the Django Admin dashboard
admin.site.register(JobDescription)
