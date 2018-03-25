from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
#from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from actstream import action
from actstream.models import Action
#from actstream.models import model_stream

from .models import Profile, Post
from .forms import CreatePostForm, ProfileForm, SignInForm, SignUpForm
# Create your views here.


def create_post(request):
    # print(request.user)
    if not request.user.is_authenticated():
        print("Not Authenticated")  #Use Message FW
        return redirect('/social/')
    form = CreatePostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            user_profile = Profile.objects.get(user=request.user)
            action.send(request.user, verb="Posted", action_object=instance)
            return redirect('/social/')
    return render(request, 'social/createpost.html', {"form": form})


def follow_others(request):
    if not request.user.is_authenticated():
        print("Login to follow others")  #Use Message FW
        return redirect('/social/signin')
    users_list = User.objects.all().exclude(username=request.user.username)
    return render(request, 'social/follow_others.html', {"users_list": users_list})


def index(request):
    return render(request, 'social/index.html', {})


def profile(request, slug):
    obj = Profile.objects.get(slug=slug)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
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


def signin(request):
    if request.user.is_authenticated():
        return redirect('/social/')
    form = SignInForm(request.POST or None)
    error_message = ""
    if request.method == "POST":
        if form.is_valid():
            user = authenticate(username=request.POST["username"],
                                password=request.POST["password"])
            # print(user)
            if user is not None:
                login(request, user)
                return redirect('/social/')
        error_message = "Please provide correct credentials"
    return render(request, 'social/signin.html', {"form": form, "errors": error_message})


def signout(request):
    logout(request)
    return redirect('/social/')


def signup(request):
    form = SignUpForm(request.POST or None)
    if request.method == "POST":
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


def view_posts(request):
    if not request.user.is_authenticated():
        return redirect('/social/signin/')
    #user_profile = Profile.objects.get(user=request.user)
    return render(request, 'social/posts.html', {'user': request.user})
