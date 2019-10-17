from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages, auth
from .forms import FeatureForm, FeatureCommentForm
from .models import Feature, FeatureComment
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create new feature view
@login_required
def new_feature(request):
    template_name='features/new.html'
    if request.method == 'POST':
        feature_form = FeatureForm(request.POST or None, request.FILES or None)
        if feature_form.is_valid():
            feature = feature_form.save(commit=False)
            feature.author = request.user
            feature = feature_form.save()
            messages.success(
                request, "Thanks, your feature request has been submitted")
            return redirect(reverse('view_all_features'))
    else:
        feature_form = FeatureForm()

    context= {'feature_form': feature_form}
    return render(request, template_name, context)

# Edit feature view
@login_required
def edit_feature(request, pk):
    template_name='features/edit.html'
    feature = get_object_or_404(Feature, pk=pk)
    if request.method == 'POST':
        feature_form = FeatureForm(request.POST, instance=feature)
        if feature_form.is_valid():
            feature = feature_form.save(commit=False)
            feature.author = request.user
            feature.save()
            messages.success(
                request, "Thanks, your feature request has been updated")
            return redirect(reverse('index'))
    else:
        feature_form = FeatureForm(instance=feature)

    context= {
        'feature_form': feature_form,
        'feature': feature,
    }
    return render(request, template_name, context)

# Delete feature view
@login_required
def delete_feature(request, pk):
    feature = get_object_or_404(Feature, pk=pk)
    feature.delete()
    messages.success(
        request, "Your feature request has been successfully deleted")
    return redirect(reverse('view_all_features'))


# See all features view
def view_all(request):
    features = Feature.objects.all()
    template_name = 'features/view_all.html'
    ordering = ['-date_posted']
    page = request.GET.get('page', 1)

    paginator = Paginator(features, 8)

    try:
        features = paginator.page(page)
    except PageNotAnInteger:
        features = paginator.page(1)
    except EmptyPage:
        features = paginator.page(paginator.num_pages)

    context= {
        'features': features
    }
    return render(request, template_name, context)

# Single feature view
def view_one(request, pk):
    template_name = 'features/view_one.html'
    feature = get_object_or_404(Feature, pk=pk)
    comments = FeatureComment.objects.filter(feature_id=feature.pk)
    user = request.user

    if request.method == 'POST':
        comment_form = FeatureCommentForm(request.POST or None)
        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.feature = feature
            comment.save()
            messages.success(
                request, "Thanks, your comment has been submitted.")
            return redirect('view_one', pk=feature.pk)
    else:
        comment_form = FeatureCommentForm()
        feature.views += 1
        feature.save()
    
    
    context= {
        'feature': feature,
        'comment_form': comment_form,
        'comments': comments,
        'user': user
    }
    return render(request, template_name, context)