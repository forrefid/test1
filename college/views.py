from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from college.models import Notice, Student, Branch
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.urls.base import reverse_lazy
from college.form import StudentForm
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from college.serializers import NoticeSerializer, StudentSerializer,\
    UserSerializer, BranchSerializer
from college.mypermissions import MyPers2

def about(request):
    return render(request, "about.html");

def contact(request):
    return render(request, "contact.html");

@method_decorator(login_required, name='dispatch')
class NoticeList(ListView):
    model = Notice
    def get_queryset(self):
        si = self.request.GET.get('si')
        if si==None:
           si=''
        if self.request.user.is_superuser:
            return Notice.objects.all().filter(subject__icontains = si).order_by('-id')
        else:
            st = Student.objects.filter(user=self.request.user.id)[0]            
            if st!=None and st.branch !=None:
                return Notice.objects.all().filter(branch=st.branch.id, subject__icontains = si).order_by('-id')
            else:
                return Notice.objects.all().filter(branch=0)
    paginate_by = 7

@method_decorator(login_required, name='dispatch')
class NoticeDetails(DetailView):
    model = Notice
    
@method_decorator(login_required, name='dispatch')
class StudentUpdate(UpdateView):
    form_class=StudentForm
    model = Student
    success_url = reverse_lazy('notice_list')     
class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all().order_by('-uploaded_at')
    serializer_class = NoticeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('-uploaded_at')
    serializer_class = StudentSerializer
    permission_classes = (MyPers2,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

