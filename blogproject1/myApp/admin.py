from django.contrib import admin

# Register your models here.
from django.contrib import admin
from myApp.models import Post,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    l=['title','slug','author','body','publish','created','updated','status']
    prepopulated_fields={'slug':['title']}
    list_filter=['status','created','publish','author']
    search_fields=['title','body']
    raw_id_fields=('author',)
    ordering=['status','publish']
class CommentAdmin(admin.ModelAdmin):
    l=['post','email','body','created','updated','active']
    list_filter=['active','created','updated']
    search_fields=['name','email','body']

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)