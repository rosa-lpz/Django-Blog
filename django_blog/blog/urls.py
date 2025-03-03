from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    # Index -  Homepage view, lists latest posts
    path('', views.index, name='index'),

    # Detail page for a single blog category -  Category view
    path('category/<int:category_id>/', views.category_page, name='category_page'),

    # Detail page for a single blog topic - Topic view
    path('topic/<int:topic_id>/', views.topic_page, name='topic_page'),

    # Detail page for a single Post -  Individual post view
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

    # Page for adding a new category
    path('new_category/', views.new_category, name='new_category'),

    # Page for adding a new topic
    path('new_topic/<int:category_id>/', views.new_topic, name='new_topic'),

    # Page for adding a new post
    path('new_post/<int:topic_id>/', views.new_post, name='new_post'),

    # Page for editing a post
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
 
]