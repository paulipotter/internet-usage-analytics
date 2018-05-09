"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from webapp import views
from django.contrib.auth import views as auth_views
admin.autodiscover()

urlpatterns = [ path('admin/', admin.site.urls),
                path('', views.home, name='home'),
                path('results/', views.results, name='results'),
                path('acknowledgements/', views.acknowledgements, name='acknowledgements')
                ]

# Debug Toolbar
if settings.DEBUG:
    #import debug_toolbar
    from django.contrib.staticfiles import views as staticviews
    from django.conf.urls.static import static
    urlpatterns += [
        #url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^static/(?P<path>.*)$', staticviews.serve),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# normalpatterns = [
#     url(r'^results/', views.results, name='results'),
#     url(r'^three/', views.three, name='three')
# ]
# urlpatterns += normalpatterns
