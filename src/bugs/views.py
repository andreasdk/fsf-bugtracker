from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages, auth
from .forms import BugForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

@login_required
def new_bug(request):
    template_name='bugs/new.html'
    if request.method == 'POST':
        bug_form = BugFormForm(request.POST)
        if bug_form.is_valid():
            bug = form.save(commit=False)
            bug.author = request.user
            bug_form.save()
            messages.success(
                request, "Thanks, your bug report has been submitted")
            return redirect(reverse('index'))
    else:
        bug_form = BugForm()

    context= {'bug_form': bug_form}
    return render(request, template_name, context)

