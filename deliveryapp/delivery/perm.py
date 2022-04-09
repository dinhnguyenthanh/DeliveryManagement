from rest_framework import permissions


class CommentOwnerPerms(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, comment):
        """
        return `True` if permission is granted, `False` otherwise.
        """
        return request.user == comment.user

