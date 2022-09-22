from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def home_page(request: HttpRequest) -> HttpResponse:
    """home page

    Args:
        request (HttpRequest): _description_

    Returns:
        HttpResponse: response
    """
    return render(request, 'home.html')
