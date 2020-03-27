from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .. import models
from django.shortcuts import get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType

class Comment(DetailView):
    model = models.Comment
    context_object_name = 'comment'
    template_name = 'judge/comment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sidebar_items'] = models.SidebarItem.objects.order_by('order')
        context['page_title'] = 'PNOJ: Comment #' + str(self.get_object().pk)
        comment_contenttype = ContentType.objects.get_for_model(models.Comment)
        context['comments'] = models.Comment.objects.filter(parent_content_type=comment_contenttype, parent_object_id=self.get_object().pk)
        return context

@require_POST
@login_required
def add_comment(request, parent_type, parent_id):
    if parent_type == 'problem':
        parent = get_object_or_404(models.Problem, slug=parent_id)
    elif parent_type == 'user':
        parent = get_object_or_404(models.User, username=parent_id)
    elif parent_type == 'submission':
        parent = get_object_or_404(models.Submission, pk=parent_id)
    elif parent_type == 'comment':
        parent = get_object_or_404(models.Comment, pk=parent_id)
    elif parent_type == 'post':
        parent = get_object_or_404(models.BlogPost, slug=parent_id)
    else:
        raise NotImplementedError
    author = request.user
    comment = models.Comment(parent=parent, text=request.POST['text'], author=author)
    comment.save()
    return redirect('comment', pk=comment.pk)