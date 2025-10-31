from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post, Comment, UserProfile, PostImage
from .forms import PostForm, CommentForm, UserProfileForm


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
    else:
        UserProfile.objects.create(user=instance)


def post_list(request):
    posts = Post.objects.select_related('author', 'author__profile').prefetch_related('likes', 'images')
    paginator = Paginator(posts, 9)  # Show 9 posts per page for grid layout
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})


def post_detail(request, slug):
    post = get_object_or_404(Post.objects.select_related('author', 'author__profile').prefetch_related('images'), slug=slug)
    comments = post.comments.select_related('author', 'author__profile').all()
    is_liked = post.likes.filter(id=request.user.id).exists() if request.user.is_authenticated else False
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('post_detail', slug=post.slug)
        else:
            messages.error(request, 'You must be logged in to comment.')
    else:
        comment_form = CommentForm()
    
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'is_liked': is_liked,
    })


@login_required
def post_like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    return JsonResponse({
        'liked': liked,
        'total_likes': post.total_likes()
    })


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            
            # Handle multiple images
            images = request.FILES.getlist('images')
            for i, image in enumerate(images):
                PostImage.objects.create(
                    post=post,
                    image=image,
                    order=i
                )
            
            messages.success(request, f'Your photos have been shared! ({len(images)} images uploaded)')
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Share Photos'})


@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.author != request.user:
        messages.error(request, 'You can only edit your own posts.')
        return redirect('post_detail', slug=post.slug)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            
            # Handle new images if uploaded
            new_images = request.FILES.getlist('images')
            if new_images:
                # Get current max order
                max_order = post.images.count()
                for i, image in enumerate(new_images):
                    PostImage.objects.create(
                        post=post,
                        image=image,
                        order=max_order + i
                    )
                messages.success(request, f'Your post has been updated! ({len(new_images)} new images added)')
            else:
                messages.success(request, 'Your post has been updated!')
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/post_edit.html', {
        'form': form, 
        'post': post,
        'title': 'Edit Photos'
    })


@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.author != request.user:
        messages.error(request, 'You can only delete your own posts.')
        return redirect('post_detail', slug=post.slug)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your photo has been deleted!')
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user).prefetch_related('likes', 'images')
    return render(request, 'blog/user_profile.html', {
        'profile_user': user,
        'posts': posts
    })


@login_required
def delete_image(request, pk):
    image = get_object_or_404(PostImage, pk=pk)
    post = image.post
    
    if post.author != request.user:
        messages.error(request, 'You can only delete images from your own posts.')
        return redirect('post_detail', slug=post.slug)
    
    if request.method == 'POST':
        image.delete()
        messages.success(request, 'Image deleted successfully!')
        
        # If no images left, redirect to post list
        if not post.images.exists():
            post.delete()
            messages.info(request, 'Post deleted as it had no images left.')
            return redirect('post_list')
        
        return redirect('post_detail', slug=post.slug)
    
    return render(request, 'blog/delete_image.html', {'image': image, 'post': post})


@login_required
def edit_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('user_profile', username=request.user.username)
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'blog/edit_profile.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in automatically after signup
            login(request, user)
            messages.success(request, 'Welcome to Tatana! Your account has been created.')
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
