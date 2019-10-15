from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

# ----- Feature Post ----- #
class Feature(models.Model):
    FEATURE_STATUS = (
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
        choices=FEATURE_STATUS,
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
    price = models.IntegerField(
        default=10,
        blank=False
    )

    class Meta:
        ordering: ('-votes')

    def __str__(self):
        return "#{0} {1}".format(
            self.id, self.title)

# ----- Feature Comment ----- #
class FeatureComment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    feature = models.ForeignKey(
        Feature,
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
        verbose_name = ("Feature Comment")
    
    def __str__(self):
        return self.comment

# ----- Feature Votes ----- #
class FeatureVotes(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    feature = models.ForeignKey(
        Feature,
        on_delete=models.CASCADE,
        null=True
    )
    price = models.IntegerField(
        default=5, 
        blank=False
    )

    def __str__(self):
        return 'Feature # {0} voted for by {1}'.format(
            self.feature.id, self.user.username)