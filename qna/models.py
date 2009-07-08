from django.db import models

class Question(models.Model):
    pub_date = models.DateTimeField('Date submitted')
    slug = models.SlugField(unique_for_date='pub_date')
    question = models.TextField()
    answer = models.TextField()
    public = models.BooleanField(default=False)
    allow_comments = models.BooleanField(default=True)

    def __unicode__(self):
        return self.question[:100]    