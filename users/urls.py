from rest_framework import routers
from django.urls import path, include

from users.views import UserViewSet

router = routers.DefaultRouter() # routing을 담당할 객체
router.register("user", UserViewSet) # UserViewSet객체에서 API 정보를 가져옴

urlpatterns = router.urls # router 객체의 urls field를 사용한다.
