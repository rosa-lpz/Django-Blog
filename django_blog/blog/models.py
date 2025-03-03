from django.db import models
import datetime


class Category(models.Model):
    # Represents one person or organization's blog
    name = models.CharField(max_length=200)

    # Extra information for managing the Category model as "categories" (in plural)
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        """Return a string representation of the blog."""
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # Extra information for managing the Topic model as "topics" (in plural)
    class Meta:
        verbose_name_plural = 'topics'

    def __str__(self):
        return self.name


# Represents an individual post. 
class Post(models.Model):
    #Reference to other record in database
    title = models.CharField(max_length=500)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    #date_added = models.DateField(datetime.date.today)
    image = models.ImageField(upload_to='blog/images/', blank=True, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    # Extra information for managing the Post model as "posts" (in plural)
    class Meta:
        verbose_name_plural = 'posts'

    def __str__(self):
        #Return a string representintg the blog post
        if len(self.title) > 50:
            return f"{self.title[:50]}..."
        else:
            return self.title