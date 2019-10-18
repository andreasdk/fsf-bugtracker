from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

# ----- Bug Post ----- #
class Bug(models.Model):
    BUG_STATUS = (
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
        ('Complete', 'Complete'))
    
    title = models.CharField(
        max_length=60,
        blank=False
    )
    description = models.TextField(
        blank=False
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    status = models.CharField(
        max_length=11,
        choices=BUG_STATUS,
        default='New' 
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    views = models.IntegerField(
        default=0
    )
    votes = models.IntegerField(
        default=0
    )

    class Meta:
        ordering: ('-votes')

    def __str__(self):
        return "#{0} {1}".format(
            self.id, self.title)

# ----- Bug Comment ----- #
class BugComment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    bug = models.ForeignKey(
        Bug,
        on_delete=models.CASCADE,
        null=True
    )
    comment = models.TextField(
        max_length=1000,
        null=True
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    class Meta:
        verbose_name = ("Bug Comment")
    
    def __str__(self):
        return self.comment

# ----- Bug Votes ----- #
class BugVotes(models.Model):
    user = models.ForeignKey(
        User,
        related_name='bug_votes',
        on_delete=models.CASCADE,
        null=True
    )
    bug = models.ForeignKey(
        Bug,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return 'Bug # {0} voted for by {1}'.format(
            self.bug.id, self.user.username)
   
    
    