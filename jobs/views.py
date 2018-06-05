# from django.shortcuts import render
from .models import Job
from django.views import generic

'''
def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})
'''


class HomeView(generic.ListView):

    template_name = 'jobs/home.html'
    context_object_name = 'all_jobs'

    def get_queryset(self):
        return Job.objects.all()
