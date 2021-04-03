from django.urls import path

from moto.website.apis import (
  OrderListCreateApi,
  OrderRetrieveUpdateApi,
  PartListCreateApi,
  PartRetrieveUpdateApi,
  CastingListCreateApi,
  CastingRetrieveUpdateApi,
  ExpeditionListCreateApi,
  ExpeditionRetrieveUpdateApi,
  StoredCastingsListCreateApi,
  StoredCastingsRetrieveUpdateApi,
  MachinedPartsListCreateApi,
  MachinedPartsRetrieveUpdateApi
)

app_name = "website_apis"
urlpatterns = [
    path("order", OrderListCreateApi.as_view(), name="order-list-create-api"),
    path("order/<int:pk>", OrderRetrieveUpdateApi.as_view(), name="order-retrieve-update-api"),
    path("part", PartListCreateApi.as_view(), name="part-list-create-api"),
    path("part/<int:pk>", PartRetrieveUpdateApi.as_view(), name="part-retrieve-update-api"),
    path("casting", CastingListCreateApi.as_view(), name="casting-list-create-api"),
    path("casting/<int:pk>", CastingRetrieveUpdateApi.as_view(), name="casting-retrieve-update-api"),
    path("expedition", ExpeditionListCreateApi.as_view(), name="expedition-list-create-api"),
    path("expedition/<int:pk>", ExpeditionRetrieveUpdateApi.as_view(), name="expedition-retrieve-update-api"),
    path("stored-castings", StoredCastingsListCreateApi.as_view(), name="stored-castings-list-create-api"),
    path("stored-castings/<int:pk>", StoredCastingsRetrieveUpdateApi.as_view(), name="stored-castings-retrieve-update-api"),
    path("machined-parts", MachinedPartsListCreateApi.as_view(), name="machined-parts-list-create-api"),
    path("machined-parts/<int:pk>", MachinedPartsRetrieveUpdateApi.as_view(), name="machined-parts-retrieve-update-api"),
]
