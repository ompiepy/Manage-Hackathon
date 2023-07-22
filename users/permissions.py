from rest_framework import permissions

# class RegistrationPermission(DjangoModelPermissions):
#     def has_permission(self, request, view):
#         user = request.user
#         if user.is_authenticated:
#             return False
#         return False


class GeneralPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_superuser:
            return True
        if request.method == 'GET':
            return True

        return False


class RegistrationPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow POST requests for unauthenticated users
        user = request.user
        if request.method == 'POST' and not request.user.is_authenticated:
            return True

        # Deny all other requests
        return False


class SubmissionPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        print(user.username)
        print(user.get_all_permissions())
        if user.is_authenticated and user.has_perm('users.add_submission_form'):
            return True

        return False
