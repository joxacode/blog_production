from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ProfileData(BaseModel):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='profile_data/')
    body = models.TextField()

    def __str__(self):
        return self.full_name


class Post(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post/')
    body = models.TextField()
    views_count = models.IntegerField()

    def __str__(self):
        return self.title


class SocialLink(BaseModel):
    name = models.CharField(max_length=255)
    url = models.URLField()
    icon = models.CharField(max_length=50)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return f'{self.name} {self.url}'


class Tool(BaseModel):
    skill = models.CharField(max_length=50)
    presentage = models.PositiveIntegerField(default=100)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return f'{self.skill} - {self.presentage}'


class About(BaseModel):
    text = models.TextField()
    donation = models.PositiveIntegerField()
    projects = models.PositiveIntegerField()
    volunteers = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.donation}"


class Service(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=30)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return self.title


class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Project(BaseModel):
    name = models.CharField(max_length=155)
    image = models.ImageField(upload_to="projects/")
    used_tools = models.ManyToManyField(Tool)
    link = models.URLField()
    description = models.TextField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

