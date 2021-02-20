from django.urls import path

from moto.website.apis import OrderListApi, OrderDetailApi

app_name = "website_apis"
urlpatterns = [
    path("orders", OrderListApi.as_view(), name="order-list-api"),
    path("order/<int:order_id>", OrderDetailApi.as_view(), name="order-details-api")
]
