from django.urls import path

from moto.website.apis import (
  OrderListCreateApi,
  OrderRetrieveUpdateApi,
  PartListCreateApi,
  PartRetrieveUpdateApi,
  CastingListCreateApi,
  CastingRetrieveUpdateApi
)

app_name = "website_apis"
urlpatterns = [
    path("order", OrderListCreateApi.as_view(), name="order-list-create-api"),
    path("order/<int:pk>", OrderRetrieveUpdateApi.as_view(), name="order-retrieve-update-api"),
    path("part", PartListCreateApi.as_view(), name="part-list-create-api"),
    path("part/<int:pk>", PartRetrieveUpdateApi.as_view(), name="part-retrieve-update-api"),
    path("casting", CastingListCreateApi.as_view(), name="casting-list-create-api"),
    path("casting/<int:pk>", CastingRetrieveUpdateApi.as_view(), name="casting-retrieve-update-api"),
]
