from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement

from advertisements.serializers import AdvertisementSerializer

from advertisements.permissions import IsAuthorOrReadOnly

from advertisements.filters import AdvertisementFilter




class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdvertisementFilter

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorOrReadOnly]
        return [permission() for permission in permissions]
