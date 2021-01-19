from django.shortcuts import render,redirect
from django.contrib.auth.forms import PasswordChangeForm #UserCreationForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from accounts.models import User
from .models import Acc, PostLike
from .forms import UserRegisterForm
from django.http import JsonResponse


# Create your views here.

def index(request):
    return render(request,'index.html')
    

def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserRegisterForm()          
    return render(request,'registration/register.html',{'form':form})

@login_required
def PasswordChange(request):
    user = User.objects.get(pk=request.user.id)
    if request.method =='POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = PasswordChangeForm(user)          
    return render(request,'registration/password_change_form.html',{'form':form})    

"""def PasswordChangeDoneView(request):
    return render(request,'registration/password_change_done.html')

def post_p(request, post_id):
    post = Acc.objects.get(pk=post_id)
    return render(request,'registration/post_p.html',{"selected_post":post})"""

def create_post(request):
    #user = User.objects.get(pk=request.user.id)
    if request.method =='POST':
        print(request.POST)
        title = request.POST["title"]
        content = request.POST["content"]
        file = request.FILES.pop('pic')
        file = file[0]
        new_post = Acc.objects.create(title=title, content=content, image=file, user_id=request.user.id)
        return redirect('all_post_url')
    return render(request,'registration/create_post.html')

@login_required
def profile(request):
    user_post = Acc.objects.filter(user=request.user)
    return render(request,'profile.html', {"user_post": user_post})

def all_post(request):
    #user = User.objects.get(pk=request.user.id)
    all_post = Acc.objects.all()
    current_user_id = request.user.id
    return render(request,'registration/all_post.html', {"all_post": all_post,"current_user_id": current_user_id})

def delete_post(request, post_id):
    post = Acc.objects.get(pk=post_id)
    if request.method =='GET':
        if post.user_id == request.user.id:
            post.delete()
    return redirect('all_post_url')

def edit_post(request, post_id):
    post = Acc.objects.get(pk=post_id)
    if request.method =='POST':
        if post.user_id == request.user.id:
            title = request.POST["title"]
            content = request.POST["content"]
            post.title = title
            post.content = content
            post.save()
        return redirect('profile_url')   
    return render(request,'registration/edit_post.html') 

def like_unlike_post(request, post_id):
    post =Acc.objects.get(pk=post_id)
    liked = False
    if request.method =='GET':
        try:
            post_like=PostLike.objects.get(post_id=post_id, user_id=request.user.id)
            post_like.delete()
        except PostLike.DoesNotExist:
            post_like=PostLike.objects.create(post_id=post_id, user_id=request.user.id)
            liked = True
    return JsonResponse({"likes": post.likes(), "liked": liked})

def edit_profile(request, user_id):
    user = User.objects.get(pk=request.user.id)
    if request.method =='POST':
        if user_id ==request.user.id:
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            username = request.POST["username"]
            profile_pic = request.FILES.pop('profile_pic')
            profile_pic = profile_pic[0]
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.profile_pic = profile_pic
            user.save()
            return redirect('profile_url')   
    return render(request,'registration/edit_profile.html')