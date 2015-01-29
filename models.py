from django.db import models
from django.contrib.auth.models import User

class Reading(models.Model):

    VOTE_CHOICES = (
        ('u', 'upvote'),
        ('d', 'downvote'),
        (NULL, 'undefined'),
    )

    user = models.ForeignKey(User)
    bookId = models.CharField(max_length=10)
    isRead = models.BooleanField()
    vote = models.ChatField(max_length=1, choices=VOTE_CHOICES)
