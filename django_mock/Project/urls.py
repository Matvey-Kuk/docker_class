from django.conf import settings
from django.conf.urls import include, url, patterns
from django.contrib import admin

from Project.forms import CustomAuthenticationForm, CustomSetPasswordForm

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^login/$',
        'django.contrib.auth.views.login',
        {'authentication_form': CustomAuthenticationForm},
        name="login"
    ),
    url(
        r'^password_reset/$',
        'django.contrib.auth.views.password_reset',
        name="password_reset",
    ),
    url(
        r'^password_reset_done/$',
        'django.contrib.auth.views.password_reset_done',
        name="password_reset_done",
    ),
    url(
        r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'set_password_form': CustomSetPasswordForm},
        name="password_reset_confirm",
    ),
    url(
        r'^password_reset_complete/$',
        'django.contrib.auth.views.password_reset_complete',
        name="password_reset_complete",
    ),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': "login"}, name="logout"),
]

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$',
                             'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
