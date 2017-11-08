from rest_framework import serializers, permissions
from college.models import Notice, Student, Branch
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes

class NoticeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notice
        fields = ('url', 'subject', 'message', 'attachment1',  'uploaded_at')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('url', 'name', 'skills', 'sem',  'uploaded_at', 'myimg', 'user', 'marks_10', 'marks_12', 'marks_aggr')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class BranchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branch
        fields = ('name', 'hod')
