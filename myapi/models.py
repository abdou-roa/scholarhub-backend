from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

from django.db import models

# Courses Model
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.CharField(max_length=100)  # Assuming instructor is just a name or ID

    def __str__(self):
        return self.course_name

# Weeks Model
class Week(models.Model):
    week_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    week_number = models.PositiveIntegerField()
    week_title = models.CharField(max_length=200)

    def __str__(self):
        return f"Week {self.week_number}: {self.week_title}"

# Topics Model
class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    topic_title = models.CharField(max_length=200)
    video_url = models.URLField(blank=True, null=True)
    pdf_url = models.URLField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)

    def __str__(self):
        return self.topic_title

# Content Model
class Content(models.Model):
    content_id = models.AutoField(primary_key=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content_slug = models.SlugField(unique=True)
    content_title = models.CharField(max_length=200)
    content_description = models.TextField()
    content_type = models.CharField(max_length=50)
    content_url = models.URLField()
    content_duration = models.DurationField(blank=True, null=True)

    def __str__(self):
        return self.content_title

# Quizzes Model
class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    quiz_title = models.CharField(max_length=200)
    total_questions = models.PositiveIntegerField()

    def __str__(self):
        return self.quiz_title

# Questions Model
class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()

    def __str__(self):
        return self.question_text

# Choices Model
class Choice(models.Model):
    choice_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

# UserProgress Model
class UserProgress(models.Model):
    progress_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    progress_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.progress_percentage}%"

# QuizAttempts Model
class QuizAttempt(models.Model):
    attempt_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    attempt_date = models.DateTimeField(auto_now_add=True)
    score = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.score}"

# ContentCompletion Model
class ContentCompletion(models.Model):
    completion_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    completion_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.content.content_title}: {'Completed' if self.is_completed else 'Not Completed'}"
