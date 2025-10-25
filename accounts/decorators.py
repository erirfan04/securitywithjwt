from django.http import HttpResponse

def role_required(allowed_roles=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            return HttpResponse("Unauthorized", status=403)
        return wrapper
    return decorator


"""
role_required(['admin']) is called → returns decorator.

decorator(admin_dashboard) is called → returns wrapper.

When user requests /admin_dashboard/, wrapper runs:

Checks authentication & role.

Runs admin_dashboard if allowed.

Returns 403 if not allowed.
"""