from django.contrib import admin

# Register your models here.
from .models import Candidate,Poll,Choice # ,Post

admin.site.register(Candidate)
admin.site.register(Poll)
admin.site.register(Choice)
