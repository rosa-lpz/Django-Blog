from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Category, Topic, Post

from blog.forms import CategoryForm, TopicForm, PostForm

def index(request):
    categories = Category.objects.all()
    topics = Topic.objects.all()
    latest_posts = Post.objects.all().order_by('-date_added')[:1]  # Get the latest post
    recent_posts = Post.objects.all().order_by('-date_added')[1:6]  # Get the next 5 recent posts
    context= {'categories': categories, 'topics':topics,
        'latest_posts': latest_posts,
        'recent_posts': recent_posts}
    return render(request, 'blog/index.html', context)
 


# Blog Category Page & Posts
def category_page(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    topics = Topic.objects.filter(category=category)
    categories = Category.objects.all()
    context= {'category': category,'topics': topics, 'categories': categories}
    return render(request, 'blog/category_page.html', context)

# Blog Topic Page & Posts
def topic_page(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    posts = Post.objects.filter(topic=topic).order_by('-date_added')
    categories = Category.objects.all()
    context = {'topic': topic, 'posts': posts, 'categories': categories}
    return render(request, 'blog/topic_page.html', context)

# Post page
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    categories = Category.objects.all()
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'categories': categories
    })


# New Category
def new_category(request):
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = CategoryForm()
    else:
        # POST data submitted; process data.
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')


    # Display a blank or invalid form
    context = {'form': form }
    return render(request, 'blog/new_category.html', context)


# New Topic - Add a new topic for a particular category blog.
def new_topic(request, category_id):
    category = Category.objects.get(id=category_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.category = category
            new_topic.save()
            return redirect('blog:category_page', category_id=category_id)

    # Display a blank or invalid form.
    context = {'category': category, 'form': form}
    return render(request, 'blog/new_topic.html', context)

# New Post -Add a new post for a particular topic
def new_post(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PostForm()
    else:
        #POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.topic = topic
            new_post.save()
            return redirect('blog:topic_page', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'blog/new_post.html', context)

# Edit Post - Edit an existing entry.
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    topic = post.topic

    if request.method != 'POST':
        # Initial request; pre-fill form with the current post.
        form = PostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
          form.save()
          return redirect('blog:post_detail', post_id=post.id)

    context = {'post': post, 'topic': topic, 'form': form}
    return render(request, 'blog/edit_post.html', context)