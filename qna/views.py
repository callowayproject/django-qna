from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden, HttpResponse
from django.contrib.auth.decorators import user_passes_test,login_required

from models import Question
from forms import QuestionForm,AskQuestionForm

@login_required
def question_create(request):
    if request.method == 'POST':
        form = AskQuestionForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponseRedirect(form.save().get_absolute_url())
    else:
        form = AskQuestionForm()
    return render_to_response('qna/create.html', {
        'form':form,
    }, context_instance=RequestContext(request))
    
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.has_perm('question.can_create') or u.is_staff or u.is_superuser)
def question_admin(request, slug):
    q = get_object_or_404(Question, slug=slug)
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES, instance=q)
        if form.is_valid():
            return HttpResponseRedirect(form.save().get_absolute_url())
    else:
        form = QuestionForm(instance=q)
    return render_to_response('qna/admin.html', {
            'question':q,
            'form':form,
        }, context_instance=RequestContext(request))   

def question_list(request):
    return render_to_response('qna/list.html', {
        'answered': Question.objects.filter(public=True),
        'unanswered': Question.objects.filter(public=False),
    }, context_instance=RequestContext(request))
    
def question_detail(request, slug):
    q = get_object_or_404(Question, slug=slug)
    return render_to_response('qna/detail.html', {
            'question':q,
    }, context_instance=RequestContext(request))