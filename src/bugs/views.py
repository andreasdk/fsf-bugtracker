from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages, auth
from .forms import BugForm, BugCommentForm
from .models import Bug, BugComment, BugVotes
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    bug = get_object_or_404(Bug, pk=pk)
    if request.method == 'POST':
        bug_form = BugForm(request.POST, instance=bug)
        if bug_form.is_valid():
            bug = bug_form.save(commit=False)
            bug.author = request.user
            bug.save()
            messages.success(
                request, "Thanks, your bug report has been updated")
            return redirect(reverse('index'))
    else:
        bug_form = BugForm(instance=bug)

    context= {
        'bug_form': bug_form,
        'bug': bug,
    }
    return render(request, template_name, context)

# Delete bug view
@login_required
def delete_bug(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    bug.delete()
    messages.success(
        request, "Thanks, your bug report has been updated")
    return redirect(reverse('view_all_bugs'))


# See all bugs view
def view_all(request):
    bugs = Bug.objects.all()
    template_name = 'bugs/view_all.html'
    page = request.GET.get('page', 1)

    paginator = Paginator(bugs, 8)

    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)

    context= {
        'bugs': bugs
    }
    return render(request, template_name, context)

# Single bug view
def view_bug(request, pk):
    template_name = 'bugs/view_one.html'
    bug = get_object_or_404(Bug, pk=pk)
    comments = BugComment.objects.filter(bug_id=bug.pk)
    user = request.user

    if request.method == 'POST':
        comment_form = BugCommentForm(request.POST or None)
        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.bug = bug
            comment.save()
            messages.success(
                request, "Thanks, your comment has been submitted.")
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

# Bug vote view
@login_required
def vote(request, pk):

    bug = get_object_or_404(Bug, pk=pk)
    if not request.user.bug_votes.filter(bug_id=pk).exists():
        bug.votes += 1
        bug.save()
        BugVotes.objects.create(user=request.user, bug=bug)
        messages.success(request, "Bug upvoted", extra_tags="alert-primary")
        return redirect('view_bug', pk=bug.pk)
    return redirect('view_bug', pk=bug.pk)
    