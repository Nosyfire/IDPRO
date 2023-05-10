from django.shortcuts import render


def home_view(request, *args, **kwargs):
    """
    It will the homepage.
    pram
    return:
    """
    return render(request, "Pages/home.html")

def positions_view(request, *args, **kwargs):
    """
    It will the homepage.
    pram
    return:
    """
    return render(request, "Pages/positions.html")