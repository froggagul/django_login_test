from rest_framework import generics, mixins, viewsets
from users.serializers import UserSerializer
from users.models import User
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin, # 모델의 list(queryset)를 return하는 객체
    mixins.RetrieveModelMixin, # 하나의 모델을 return하는 객체
    ):
    queryset = User.objects.all() # viewset에서 다룰 data
    serializer_class = UserSerializer # 데이터의 validation을 수행하는 serializer
    permission_classes = [] # 해당 데이터에 접속 가능한 permission을 부여한다.
