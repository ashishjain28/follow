from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import Profile

from .forms import SignUpForm, ProfileForm
# Create your views here.


def index(request):
    return render(request, 'social/index.html', {})


def profile(request, slug):
    obj = Profile.objects.get(slug=slug)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            print(instance)
            instance.save()
            return redirect('/social/')
        else:
            return render(request, 'social/profile.html', {"form": form})
    profile_instance = get_object_or_404(Profile, slug=slug)
    instance = get_object_or_404(User, username=profile_instance.user)
    initial = {'first_name': instance.first_name,
               'last_name': instance.last_name,
               'email': instance.email,
               'mobile_number': profile_instance.mobile_number,
               'is_mobile_visible': profile_instance.is_mobile_visible,
               'is_email_visible': profile_instance.is_email_visible,
               'image': profile_instance.image
               }
    form = ProfileForm(initial=initial)
    context = {
        "form": form
    }
    return render(request, 'social/profile.html', context)


def signup(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=True)
        profile_instance = Profile()
        profile_instance.user = instance
        profile_instance.mobile_number = form["mobile_number"].value()
        profile_instance.friend_requests_received = []
        profile_instance.friend_requests_sent = []
        profile_instance.friends = []
        profile_instance.save()
        return redirect('/social/')
    context = {
        "form": form
    }
    return render(request, 'social/signup.html', context)
