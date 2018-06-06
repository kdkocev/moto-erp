from django.urls import path

from moto.website.apis import OrderListApi

app_name = "website_apis"
urlpatterns = [
    path("orders", OrderListApi.as_view(), name="order-list-api")
]
