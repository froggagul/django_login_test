from importlib.resources import path

from django.urls import path, include
from auth.views import MeView

urlpatterns = [
    path('me/', MeView.as_view()),
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls'))
]
