from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import generics

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

#model
from .models import Course
from .models import Week
from .models import Topic
from .models import Content
from .models import Quiz
from .models import Question
from .models import Choice

# serilaizer
from .serializers import UserRegisterSerializer
from .serializers import UserLoginSerializer
from .serializers import CourseSerializer
from .serializers import WeekSerializer
from .serializers import TopicSerializer
from .serializers import ContentSerializer
from .serializers import QuizSerializer
from .serializers import QuizQuestionSerializer
from .serializers import QuizQuestionChoiceSerializer

class UserLoginAPIView(APIView):
    def post(self, request, *args, **kargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = request.data.get('username')
            password = request.data.get('password')

            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                response = {
                    'success': True,
                    'username': user.username,
                    'email': user.email,
                    'token': token.key
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                # Invalid login credentials
                return Response({
                    "detail": "Invalid username or password"
                }, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterAPIView(APIView):
    def post(self, request, *args, **kargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'user': serializer.data,
                'token': Token.objects.get(user=User.objects.get(username=serializer.data['username'])).key
            }
            return Response(response, status=status.HTTP_200_OK)
        raise ValidationError(
            serializer.errors, code=status.HTTP_406_NOT_ACCEPTABLE)


class UserLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({"success": True, "detail": "Logged out!"}, status=status.HTTP_200_OK)
    

class CourseAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]  


class WeekAPIView(generics.ListAPIView):
    serializer_class = WeekSerializer
    permission_classes = [IsAuthenticated]  
    def get_queryset(self):
        course_id = self.kwargs['course_id']  
        return Week.objects.filter(course_id=course_id)
    
class TopicAPIView(generics.ListAPIView):
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]  
    def get_queryset(self):
        week_id = self.kwargs['week_id']  # Assuming you pass week_id in URL
        return Topic.objects.filter(week_id=week_id)
    
class ContentTopicAPIView(generics.ListAPIView):
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticated]  
    def get_queryset(self):
        topic = self.kwargs['topic']  # Assuming you pass week_id in URL
        return Content.objects.filter(topic=topic)

class ContentAPIView(generics.ListAPIView):
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        content_slug = self.kwargs['content_slug']
        return Content.objects.filter(content_slug=content_slug)
    
class QuizAPIView(generics.ListAPIView):
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        quiz_topic = self.kwargs['topic']
        return Quiz.objects.filter(topic=quiz_topic)

class QuizQuestionAPIView(generics.ListAPIView):
    serializer_class = QuizQuestionSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        quiz = self.kwargs['quiz']
        return Question.objects.filter(quiz=quiz)
    

class QuizQuestionChoiceAPIView(generics.ListAPIView):
    serializer_class = QuizQuestionChoiceSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        question = self.kwargs['question']
        return Choice.objects.filter(question=question)