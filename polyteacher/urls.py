"""
URL configuration for polyteacher project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from translator.views import index, contact
from translator.views import FrenchSpanishTranslationViewSet
from translator.views import FrenchEnglishTranslationViewSet
from translator.views import Alltranslaition
from translator.views import DeutshtoFrench
from translator.views import ArameentoFrench

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('contact',contact),
    path('api/monlienversmestraductions',Alltranslaition.as_view()),
    path('api/french_spanish_translator', FrenchSpanishTranslationViewSet.as_view(), name='french_spanish_translator'),
    path('api/french_english_translator', FrenchEnglishTranslationViewSet.as_view(), name='french_english_translator'),
    path('api/deutsh_french_translator', DeutshtoFrench.as_view(), name='deutsh_french_translator'),
    path('api/arameen_french_translator', ArameentoFrench.as_view(), name='arameen_french_translator'),

]
