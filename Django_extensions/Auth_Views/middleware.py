'''
To jest Middleware, które ogranicza dostęp userów do stron niewymienionych
w LOGIN_EXEMPT_URLS w sekcji settings.py
'''

# # # Umieść to gdzieś w jakimś sensownym miejscu. Ja daję do folderu głównego
# z nazwą apki i subfolderu 'special', jako middleware.py'.
import re
from django.conf import settings
from django.shortcuts import redirect

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')

        if not request.user.is_authenticated:
            if not any(url.match(path) for url in EXEMPT_URLS):
                return redirect(settings.LOGIN_URL)


# # # To umieść w settings.py # # #
# Poniżej dane do ustawień Middleware blokującego strony przed niezalogowanymi.
LOGIN_URL = '/'

# To zwykły regex. Uważaj co wpisujesz, żeby nie wybrać całej strony.
# Te linki są DOSTĘPNE dla ludzi z zewnątrz. Cała reszta jest poblokowana.
LOGIN_EXEMPT_URLS = (
     r'^/$',
     r'^strona/.*$',
     r'^rekruter/logger/$',
     r'^rekruter/register/$',
     r'^static/.*$',
     r'^media/.*$',
)

# # # To zmień i umieść w settings.py w sekcji Middleware na końcu # # #
'ścieżka.do.twojego.middleware.LoginRequiredMiddleware'
