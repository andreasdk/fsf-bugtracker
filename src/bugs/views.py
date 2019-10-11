from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages, auth
from .forms import BugForm, BugCommentForm
from .models import Bug, BugComment
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create new bug view
@login_required
def new_bug(request):
    template_name='bugs/new.html'
    if request.method == 'POST':
        bug_form = BugForm(request.POST or None, request.FILES or None)
        if bug_form.is_valid():
            bug = bug_form.save(commit=False)
            bug.author = request.user
            bug = bug_form.save()
            messages.success(
                request, "Thanks, your bug report has been submitted")
            return redirect(reverse('profile'))
    else:
        bug_form = BugForm()

    context= {'bug_form': bug_form}
    return render(request, template_name, context)

# Edit bug view
@login_required
def edit_bug(request, pk):
    template_name='bugs/edit.html'
    bug = get_object_or_404(Bug, pk)
    if request.method == 'POST':
        bug_form = BugForm(request.POST, instance=bug)
        if bug_form.is_valid():
            bug = bug_form.save(commit=False)
            bug.author = request.user
            bug_form.save()
            messages.success(
                request, "Thanks, your bug report has been updated")
            return redirect(reverse('index'))
    else:
        bug_form = BugForm(instance=bug)

    context= {'bug_form': bug_form}
    return render(request, template_name, context)

# See all bugs view
def view_all(request):
    bugs = Bug.objects.all()
    template_name = 'bugs/view_all.html'
    ordering = ['-date_posted']
    paginate_by = 8
    context= {
        'bugs': bugs
    }
    return render(request, template_name, context)

# Single bug view
def view_one(request, pk):
    template_name = 'bugs/view_one.html'
    bug = get_object_or_404(Bug, pk=pk)
    comments = BugComment.objects.filter(bug_id=bug.pk)
    user = User.objects.get(email=request.user.email)

    if request.method == 'POST':
        comment_form = BugCommentForm(request.POST or None)
        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.bug = bug
            comment.save()
            messages.success(
                request, "Thanks, your comment has been submitted for moderation")
            return redirect('view_one', pk=bug.pk)
    else:
        comment_form = BugCommentForm()
        bug.views += 1
        bug.save()
    
    
    context= {
        'bug': bug,
        'comment_form': comment_form,
        'comments': comments,
        'user': user
    }
    return render(request, template_name, context)