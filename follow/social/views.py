from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import Profile

from .forms import SignUpForm, ProfileForm
# Create your views here.


def index(request):
    return render(request, 'social/index.html', {})


def profile(request, slug):
    form = ProfileForm(request.POST or None, request.files or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    instance = Profile.objects.get_object_or_404(slug=slug)
    form.fields["first_name"] = instance.user.first_name
    form.fields["last_name"] = instance.user.last_name
    form.fields["email"] = instance.user.email
    form.fields["mobile_number"] = instance.mobile_number
    form.fields["image"] = instance.image
    form.fields["is_mobile_visible"] = instance.is_mobile_visible
    form.fields["is_email_visible"] = instance.is_email_visible
    context = {
        form: 'form'
    }
    return render(request, 'social/profile.html', context)


def signup(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=True)
        profile_instance = Profile()
        profile_instance.user = instance
        profile_instance.mobile_number = form["mobile_number"].value()
        print(profile_instance.mobile_number)
        profile_instance.friend_requests_received = []
        profile_instance.friend_requests_sent = []
        profile_instance.friends = []
        profile_instance.save()
        print(profile_instance.friend_requests_sent)
        return redirect('/social/')
    context = {
        "form": form
    }
    return render(request, 'social/signup.html', context)
