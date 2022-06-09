from django.shortcuts import render


def google_login(request):
    """ Google signin page
    """

    return render(request, 'oauth/google_login.html')
