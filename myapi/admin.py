# admin.py
from django.contrib import admin
from .models import Course, Week, Topic, Content, Quiz, Question, Choice, UserProgress, QuizAttempt, ContentCompletion

admin.site.register(Course)
admin.site.register(Week)
admin.site.register(Topic)
admin.site.register(Content)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(UserProgress)
admin.site.register(QuizAttempt)
admin.site.register(ContentCompletion)
