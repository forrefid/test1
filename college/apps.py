from django.apps import AppConfig


class CollegeConfig(AppConfig):
    name = 'college'
    def ready(self):
            #startup code here 
            import college.mysignals
