from django.db import models

class TextData(models.Model):
    original_text = models.TextField()
    summary_text = models.TextField()
    wordcloud = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_text[:50]
