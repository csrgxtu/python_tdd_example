from django.http import HttpRequest, HttpResponse


# Create your views here.
def home_page(request: HttpRequest) -> HttpResponse:
    """home page

    Args:
        request (HttpRequest): _description_

    Returns:
        HttpResponse: response
    """
    return HttpResponse('<html><title>To-Do lists</title></html>')
