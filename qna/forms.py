from django import forms
from models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question

class AskQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title','question','allow_comments')