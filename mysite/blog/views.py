from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
#create a variable for our QuerySet: posts.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')


#render function we have one parameter request (everything we receive from the user via the Internet) and another giving the template file ('blog/post_list.html').
    return render(request, 'blog/post_list.html', {'posts': posts})
