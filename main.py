from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path

settings.configure(ROOT_URLCONF=__name__, DEBUG=True)


def hello(request):
    return HttpResponse("Hello!")


urlpatterns = [path("", hello)]

application = WSGIHandler()

if __name__ == "__main__":
    execute_from_command_line()
