from django.db import models

class User(models.Model):
    name          = models.CharField(max_length=20)
    login         = models.CharField(max_length=20, unique=True)
    password      = models.CharField(max_length=30)
    email         = models.EmailField(max_length=50, unique=True)
    profile_image = models.ImageField(max_length=255, 
                                      upload_to='media/profile_images', 
                                      default='media/default_profile_image', 
                                      null=True, blank=True)

    def __str__(self):
        return self.name

# class Tag(models.Model):
#     title         = models.CharField(max_length=30, null=False)

#     def __str__(self):
#         return self.title

# class Post(models.Model):
#     title         = models.CharField(max_length=30)
#     content       = models.TextField()
#     user_id       = models.ForeignKey(User, on_delete=models.CASCADE)
#     tags          = models.ManyToManyField(Tag)
#     picture = models.ImageField(max_length=255, 
#                                 upload_to='media/post_images', 
#                                 default='media/default_post_image', 
#                                 null=True, blank=True)

#     def __str__(self):
#         return self.title

