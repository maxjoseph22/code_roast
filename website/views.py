from django.shortcuts import render, HttpResponse

from submissions.models import Submission

# Create your views here.
def home(request):
    return render(request, "website/home.html", 
                {"submissions": Submission.objects.all()})