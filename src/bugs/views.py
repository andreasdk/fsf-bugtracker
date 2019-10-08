from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages, auth
from .forms import BugForm
from .models import Bug
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

@login_required
def new_bug(request):
    template_name='bugs/new.html'
    if request.method == 'POST':
        bug_form = BugForm(request.POST or None, request.FILES or None)
        if bug_form.is_valid():
            bug = form.save(commit=False)
            bug.author = request.user
            bug = form.save()
            messages.success(
                request, "Thanks, your bug report has been submitted")
            return redirect(reverse('profile'))
    else:
        bug_form = BugForm()

    context= {'bug_form': bug_form}
    return render(request, template_name, context)

@login_required
def edit_bug(request, pk):
    template_name='bugs/edit.html'
    bug = get_object_or_404(Bug, pk)
    if request.method == 'POST':
        bug_form = BugForm(request.POST, instance=bug)
        if bug_form.is_valid():
            bug = form.save(commit=False)
            bug.author = request.user
            bug_form.save()
            messages.success(
                request, "Thanks, your bug report has been updated")
            return redirect(reverse('index'))
    else:
        bug_form = BugForm(instance=bug)

    context= {'bug_form': bug_form}
    return render(request, template_name, context)
