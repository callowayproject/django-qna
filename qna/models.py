from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField('Date submitted',auto_now_add=True)
    slug = models.SlugField(unique=True)
    question = models.TextField()
    answer = models.TextField()
    public = models.BooleanField(default=False)
    allow_comments = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('question_detail', None, {
            'slug': self.slug
        })
        
    def save(self, *a, **kw):
        if not self.slug:
            from django.template.defaultfilters import slugify
            self.slug = slugify(self.title)[:50]
        super(Question, self).save(*a, **kw)