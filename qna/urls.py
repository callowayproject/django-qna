from django.conf.urls.defaults import *

urlpatterns = patterns('qna.views',
    url(r'^ask/$', 'question_create', name='question_create'),    
    url(r'^(?P<slug>[-\w]+)/admin/$', 'question_admin', name='question_admin'),
    url(r'^(?P<slug>[-\w]+)/$', 'question_detail', name='question_detail'),
    url(r'^$', 'question_list', name='question_list'),    
)
