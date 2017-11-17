from django.contrib import admin
from .models import collections,Post,User

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    filter_horizontal=('collection',)

admin.site.register(collections)
admin.site.register(Post,PostAdmin)
admin.site.register(User)
