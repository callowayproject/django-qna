from models import Question
from django.contrib import admin

class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    class Media:
        js = ('/media/fckeditor/fckeditor.js','/media/fckeditor/fckareas.js')
    
admin.site.register(Question, QuestionAdmin)
