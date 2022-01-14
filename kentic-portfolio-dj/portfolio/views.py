from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.conf import settings

from .models import Post
def index(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        subject = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']


        send_mail(subject , message , settings.EMAIL_HOST_USER , [email] , fail_silently=False)
        return render(request , 'index.html', {  
            'email': email, 
        'message': message})
    context = {
        'posts': posts,
      
    }
    return render(request , 'index.html', context)