from django.contrib import admin

# Register your models here.
from .models import detail

#admin.site.register(detail)

@admin.register(detail)
class detail_admin(admin.ModelAdmin):

    #fields=[]
    search_fields=['username']
    #lists
    list_display=['username','password','login_date']
    list_filter=['login_date']
