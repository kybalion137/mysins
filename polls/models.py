from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    goal = models.CharField(max_length=30)
    work = models.CharField(max_length=30)
    tg = models.URLField()

class Tishki(models.Model):
    name = models.CharField(max_length=20)
    photo = models.TextField(default="https://lh3.googleusercontent.com/1ngFfo9Xjg4K5zUd46YxfUCE8VKcsTAKvy2zyUW5tI2wqYKIZMMI9RY8vdeY64JqoOMG1od13l1xDWkKyeHSzV0TktcdlvcVxXlMKHBbw4B1x9-ermtU0Fio1O-sgcc6t9DnfgFnGGm-GlkrVx8xjgxtXmHOkZ54yCtVYF")
    fileId = models.IntegerField(default=1)