from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

# Tu jest założenie, że rozszerzony manager jest w tym samym folderze.
# Wstaw ją do models.py w jakiejś apce.
from .managers import UserManager


# Klasa zmienia autentykację Usera na email jak w Core2 i wielu innych.
# Dodaje też nowe pola. Najlepiej ją wstawić na początku projektu.
# Zależy od UserManagera.
class User(AbstractBaseUser, PermissionsMixin):
    # Pole autentykujące musi mieć "unique=True".
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    quarter = models.CharField(_('quarter'), max_length=2, blank=True)

    objects = UserManager()

    # Tutaj ustalasz które pole posłuży do autentykacji zamiast username.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

# # # Zmień odpowiednio i dodaj to do settings.py # # #
# To mówi Django, żeby zamiast standardowego modelu używał powyższego


AUTH_USER_MODEL = 'nazwa_apki.User'

# # # Zarejestruj ją jeszcze normalnie w admin.py
from .models import User
admin.site.register(User)
