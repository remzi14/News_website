from django.contrib import admin
from .models import News,Category,Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','slug','category','status','created_at','uptade_at','publish_time']
    list_filter = ['category','status']
    prepopulated_fields = {"slug":("title",)}






class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_filter = ['name']




admin.site.register(News,NewsAdmin)
admin.site.register(Category,CategoryAdmin)









