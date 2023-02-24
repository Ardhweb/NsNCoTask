from multiprocessing.connection import Client
from django.shortcuts import render

# Create your views here.
from .forms import LoginForm ,RegistrationForm
from django.db.models.signals import post_save
from . import signals
from .signals import create_client ,save_client

def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid ():
            new_user = user_form.save(commit=False)

            new_user.set_password(user_form.cleaned_data['password'])

            new_user.save()
            #Client.objects.create(user=new_user)
            post_save.connect(create_client, new_user)
            post_save.connect(save_client, new_user)
            return render(request,'register_done.html',{'new_user': new_user})
    else:
        user_form = RegistrationForm()
    return render(request,'register.html',{'user_form': user_form})