from django.contrib import admin
from college.models import Notice, Branch, Student

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('subject', 'uploaded_at')
    list_filter = ['uploaded_at', 'branch']
    search_fields = ['subject', 'message']
admin.site.register(Notice, NoticeAdmin)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'hod')
admin.site.register(Branch, BranchAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'sem')
    list_filter = ['branch', 'sem', 'marks_10', 'marks_12', 'marks_aggr']
    search_fields = ['skills', 'name']
admin.site.register(Student, StudentAdmin)
