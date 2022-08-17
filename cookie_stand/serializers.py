from rest_framework import serializers
from .models import CookieStand


class CookieSerializer(serializers.ModelSerializer):

    owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = CookieStand
        fields = ["location", "owner", "description", "hourly_sales", "minimum_customers_per_hour", "maximum_customers_per_hour", "average_cookies_per_sale"]
