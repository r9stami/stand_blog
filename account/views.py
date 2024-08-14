import uuid
from random import randint

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse

from django.views.generic import View, TemplateView, FormView
from pyexpat.errors import messages

import account.authentication
from account.forms import ContactForm, LoginForm, ProfileForm, SignUpForm
from account.models import Otp, User


class Contact(View):
    def get(self,request):
        form = ContactForm()
        return render(request ,'account/contact.html',{'form':form})

    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.get(request, 'Your message has been sent.')
            return redirect('home:main')
        return render(request ,'account/contact.html',{'form':form})


class About(TemplateView):
    template_name = 'account/about.html'


class LogoutView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        return redirect('home:main')


class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request ,'account/login.html',{'form':form})

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,phone=cd['phone'],password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home:main')
            else:
                form.add_error('phone','something wrong')

        return render(request ,'account/login.html',{'form':form})


class SignUpView(View):
    def get(self,request):
        form = SignUpForm()
        return render(request, 'account/signup.html', {'form':form})

    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd is not None:
                user = User.objects.create_user(first_name=cd['first_name'],last_name=cd['last_name']
                                                ,phone=cd['phone'],email=cd['email'],password=cd['password'])
                login(request,user)
                return redirect('home:main')
            else:
                form.add_error('phone','something wrong')

        return render(request, 'account/signup.html', {'form':form})


class UpdateProfileView(LoginRequiredMixin,View):
    def get(self,request):
        form = ProfileForm(instance=request.user)
        return render(request,'account/profile.html',{'form':form})

    def post(self,request):
        form = ProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.image = request.user.image

            instance.save()

            return redirect('home:main')
        return render(request ,'account/profile.html',{'form':form})
