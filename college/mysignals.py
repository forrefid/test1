from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from college.models import Student
from django.contrib.auth.signals import user_logged_in
from college.myctxproc import set_st
# from college.myctxproc import set_st

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance, name=instance.username)

@receiver(user_logged_in)
def get_stu_details(sender, user, request, **kwargs):
    if user.is_staff:
        st=None
    else:    
        st = Student.objects.filter(user=request.user.id)[0]
    set_st(st)
# user_logged_in.connect(get_stu_details)
