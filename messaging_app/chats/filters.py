import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    start_date = django_filters.DateTimeFilter(
        field_name='sent_at', lookup_expr='gte'
    )
    end_date = django_filters.DateTimeFilter(
        field_name='sent_at', lookup_expr='lte'
    )
    participant = django_filters.CharFilter(
        field_name='conversation__participants__email',
        lookup_expr='icontains'
    )

    class Meta:
        model = Message
        fields = ['start_date', 'end_date', 'participant']
