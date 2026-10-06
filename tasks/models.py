from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # unfinished tasks first, newest on top
        ordering = ["done", "-created"]

    def __str__(self):
        return self.title
