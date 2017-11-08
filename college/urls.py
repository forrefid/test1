from django.conf.urls import url, include
from django.contrib import admin
from college import views
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter() 
router.register(r'notices', views.NoticeViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'branchs', views.BranchViewSet)


urlpatterns = [
    url(r'^about/', views.about), 
    url(r'^contact/', views.contact),
    url(r'^$', views.NoticeList.as_view(), name='notice_list'),
    url(r'^(?P<pk>\d+)$', views.NoticeDetails.as_view(), name='notice_detail'),    
    url(r'^student/edit/(?P<pk>\d+)$', views.StudentUpdate.as_view(), name='student_edit'),           
    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),      
]
