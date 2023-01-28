from django.db import models

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        if len(self.text) < 50:
            return self.text
        else:
            return f"{self.text[:50]}..."