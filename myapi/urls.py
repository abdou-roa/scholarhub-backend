from django.urls import path
#views
from .views import UserLoginAPIView
from .views import UserRegisterAPIView
from .views import UserLogoutAPIView
from .views import CourseAPIView
from .views import WeekAPIView
from .views import TopicAPIView
from .views import ContentAPIView
from .views import QuizAPIView
from .views import ContentTopicAPIView
from .views import QuizQuestionAPIView
from .views import QuizQuestionChoiceAPIView

urlpatterns = [
    path("login/", UserLoginAPIView.as_view(), name="user_login"),
    path("register/", UserRegisterAPIView().as_view(), name="user_register"),
    path("logout/", UserLogoutAPIView.as_view(), name="user_logout"),
    path('courses/', CourseAPIView.as_view(), name='course-list'),
    path('courses/<int:course_id>/weeks/', WeekAPIView.as_view(), name='week-list'),
    path('weeks/<int:week_id>/topics/', TopicAPIView.as_view(), name='topic-list'),
    path('topic/<int:topic>/content', ContentTopicAPIView.as_view(), name="topic-content"),
    path('content/<str:content_slug>/', ContentAPIView.as_view(), name='content-list'),
    path('quiz/<int:topic>', QuizAPIView.as_view(), name='topic-quiz'),
    path('quiz/<int:quiz>/questions/', QuizQuestionAPIView.as_view(), name='quiz-question'),
    path('quiz/question/<int:question>/choices', QuizQuestionChoiceAPIView.as_view(), name='question-choices')
]