from rest_framework.permissions import BasePermission, SAFE_METHODS



class IsAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in ['GET']:  # для чтения — разрешены любые запросы
            return True

        return obj.creator == request.user