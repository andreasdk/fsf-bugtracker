from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

# ----- Bug Status ----- #
class BugStatus(models.Model):
    BUG_STATUS = (
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Complete', 'Complete'))

    bug_status = models.CharField(
        max_length=11,
        unique=True,
        choices=BUG_STATUS
    )

    class Meta:
        verbose_name = ("Bug Status")
        
    def __str__(self):
        return self.bug_status

# ----- Bug Post ----- #
class Bug(models.Model):
    
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
    status = models.ForeignKey(
        BugStatus,
        on_delete=models.CASCADE,
        null=True 
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
        return self.title
