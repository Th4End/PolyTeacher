from django.contrib import admin
from django.urls import path
# from translator.views import index, contact
# from translator.views import FrenchSpanishTranslationViewSet
# from translator.views import FrenchEnglishTranslationViewSet
# from translator.views import Alltranslaition
# from translator.views import DeutshtoFrench
# from translator.views import ArameentoFrench
from translator.views import TranslationAPIView
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/translations/', TranslationAPIView.as_view(), name='translations'),
    path('', lambda request: HttpResponse("Documentation Redhoc : /api/translations/ [GET, POST]"))








    # path('admin/', admin.site.urls),
    # path('', index),
    # path('contact',contact),
    # path('api/monlienversmestraductions',Alltranslaition.as_view()),
    # path('api/french_spanish_translator', FrenchSpanishTranslationViewSet.as_view(), name='french_spanish_translator'),
    # path('api/french_english_translator', FrenchEnglishTranslationViewSet.as_view(), name='french_english_translator'),
    # path('api/deutsh_french_translator', DeutshtoFrench.as_view(), name='deutsh_french_translator'),
    # path('api/arameen_french_translator', ArameentoFrench.as_view(), name='arameen_french_translator'),

]
