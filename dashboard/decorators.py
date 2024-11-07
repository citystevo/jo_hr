from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from functools import wraps
from django.contrib import messages

def auth_users(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard-index')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper


def allowed_users(allowed_roles=[]):
    def decorators(view_func):
        def wrapper(request, *args, **kwargs):
            # First check if user is superuser
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
                
            # Then check group permissions
            if request.user.groups.filter(name__in=allowed_roles).exists():
                return view_func(request, *args, **kwargs)
            
            return HttpResponse('You are not authorized to view this page. <a href="/index/">Click here to go back to dashboard</a>')
        return wrapper
    return decorators




def can_edit_user_data(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name='SuperAdmin').exists():
            return view_func(request, *args, **kwargs)
        if request.method == 'GET':
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return wrapper



def leave_manager_only(view_func):
    def wrapper_function(request, *args, **kwargs):       
        if request.user.is_superuser or request.user.groups.filter(name__in=['Superuser', 'Leave Manager']).exists():
            return view_func(request, *args, **kwargs)
        messages.error(request, 'You are not authorized to view this page.')
        return redirect('dashboard-index')
    return wrapper_function




# def leave_manager_only(view_func):
#     def wrapper_function(request, *args, **kwargs):       
#         if request.user.groups.filter(name__in=['Superuser', 'Leave Manager']).exists():
#             return view_func(request, *args, **kwargs)
#         messages.error(request, 'You are not authorized to view this page.')
#         return redirect('dashboard-index')
#     return wrapper_function


def can_manage_leave(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name__in=['Leave', 'Admin', 'SuperAdmin', 'Superuser', 'Leave Manager', 'Customers']).exists():
            return view_func(request, *args, **kwargs)
        messages.error(request, 'You need leave management permissions to perform this action.')
        return redirect('dashboard-index')
    return wrapper