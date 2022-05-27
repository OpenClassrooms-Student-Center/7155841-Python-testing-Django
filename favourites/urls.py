from django.urls import path
from .views import markFavourite, FavouriteProductListView


urlpatterns = [
    path('', FavouriteProductListView.as_view(), name='favourite-products'),
    path('mark/<int:id>/', markFavourite, name='mark-favourite'),
]
 