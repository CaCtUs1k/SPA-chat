from django.shortcuts import render, redirect

from main.forms import CommentForm
from main.models import Comment


def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            parent_comment_id = request.POST.get('parent_comment')
            if parent_comment_id:
                parent_comment = Comment.objects.get(pk=parent_comment_id)
                form.instance.parent_comment = parent_comment
            form.save()
            return redirect('view_comments')
    else:
        form = CommentForm()

    return render(request, 'comments/add_comment.html', {'form': form})


def view_comments(request):
    comments = Comment.objects.filter(parent_comment=None)  # Получение корневых комментариев (без родителя)
    return render(request, 'comments/view_comments.html', {'comments': comments})
