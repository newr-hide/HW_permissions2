from django_filters import rest_framework as filters, DateFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    created_at_before = filters.DateFilter(field_name='created_at', lookup_expr='lt')
    creator = filters.NumberFilter(field_name='creator_id')
    

    class Meta:
        model = Advertisement
        fields = ['creator','created_at_before']

