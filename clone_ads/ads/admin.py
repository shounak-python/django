from django.contrib import admin
from .models import Ad, Fav, Comment

# Register your models here.
admin.site.register(Ad)
admin.site.register(Fav)
admin.site.register(Comment)
