from django.shortcuts import redirect


def notLoggedUser(view_func):

    def wrapperFunc(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapperFunc

def allowedUsers(allowedGroups=[]):
    def decorator(view_func):
        def wrapperFunc(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowedGroups:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('users/')
        return wrapperFunc
    return decorator

def forAdmin(view_func):

    def wrapperFunc(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'admin':
            return view_func(request, *args, **kwargs)
        if group == 'customers':
            return redirect('userProfile')

    return wrapperFunc