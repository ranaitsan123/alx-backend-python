import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(field_name="sender__username")
    date_from = django_filters.DateTimeFilter(field_name="sent_at", lookup_expr="gte")
    date_to = django_filters.DateTimeFilter(field_name="sent_at", lookup_expr="lte")

    class Meta:
        model = Message
        fields = ["user", "date_from", "date_to"]
