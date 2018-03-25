from django.contrib import admin
from . models import Post
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated","timestamp"]
    list_display_links = ["updated"]
    list_filter = ["updated", "timestamp"]
    list_editable = ["title"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post




admin.site.register(Post, PostModelAdmin)





# Few lines for CRUD inside django shell -  Don't forget to import the model first and User

#from blog.models import Post  //// from django.contrib.auth.models import User ///
#me = User.objects.get(username='damjan') /// from django.utils import timezone ///
# Post.objects.all() ///  Post.objects.create(author=me, title='Sample title', text='Test')
# User.objects.all() // Post.objects.filter(author=me)
#  Post.objects.filter(title__contains='any variable')
# Post.objects.filter(published_date__lte=timezone.now())
# Post.objects.order_by('created_date') //
# Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
