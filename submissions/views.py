from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

from .models import Submission

# Create your views here.
def submission_detail(request, id):
    submission = get_object_or_404(Submission, pk=id)
    return render(request, "submissions/submission_detail.html", {"submission": submission})

#SubmissionForm below will call the Submission model and create a form based on that model
SubmissionForm = modelform_factory(Submission, exclude=[])

def new(request):
    if request.method == "POST":
        #form has been submitted so process data
        form = SubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        # if the form is not valid, then it will return the new form (below) 
        # but with warnings on it to fix invalidity.
    else:
        # i.e. in this case the request method must be GET, so just render the form
        form = SubmissionForm()
    return render(request, "submissions/new.html", {"form": form} )