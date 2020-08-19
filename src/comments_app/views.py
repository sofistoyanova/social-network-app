# from django.shortcuts import render
# from .models import Comment
# from django.shortcuts import render, get_object_or_404, redirect
# from django.http import Http404, HttpResponse
#
#
# # def delete_comment(request, id):
# #     comment = get_object_or_404(Comment, id=id)
# #     if comment.user != request.user:
# #         response = HttpResponse('no permission for deleting the comment')
# #         response.status_code = 403
# #         return response
# #
# #     comment.delete()
# #     post_id = comment.content_object.id
# #     return redirect('posts_app:post-details', id=post_id)
