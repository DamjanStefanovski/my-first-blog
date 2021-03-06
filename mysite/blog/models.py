# So basically the idea is to describe real things in code with properties (called object properties) and actions (called methods).
# A model in Django is a special kind of object – it is saved in the database
#  a model in the database as a spreadsheet with columns (fields) and rows (data)



from django.db import models
from django.utils import timezone


class Post(models.Model):  #this line defines our model (it is an object)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # models.ForeignKey – this is a link to another model.     #defining the properties of title, text, created_date, published_date , author
    title = models.CharField(max_length=200)
    text = models.TextField()
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):  #this is a function/method and publish is the name of the method
        self.title
        self.save()
#indent methods inside the class
    def __str__(self):
        return self.title


# To let Django know about the models created and in order to create tables for the models in our database,
# python manage.py makemigration blog - command will do just that.

# In the shell Querysets can be checked with Post.objects.all() command after importing the Post from blog.models
# for p in Post.objects.raw('SELECT * FROM blog_post'):
#...     print(p)
