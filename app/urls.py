from django.urls import path,include
from .views import *

urlpatterns = [
    path("catgeory/",ListCategory.as_view(),name="catgeroy"),
    path("detailcategory/<int:pk>",DetailsCategory.as_view(),name="detailcategory"),
    path("listproduct/",ListProduct.as_view(),name="listproduct"),
    path("detailsproduct/<int:pk>",DetailsProduct.as_view(),name="detailproduct"),
    path("listcart/",ListCart.as_view(),name="listcart"),
    path("detailscart/<int:pk>",DetailCart.as_view(),name="detailcart"),

    path("allCat/",ShowAllCategory,name="showallcat"),
    path("allpro/",ShowAllProduct,name="showallpro"),
    path("EditCat/<int:pk>",EditCategory,name="editcat"),
    path("Editpro/<int:pk>",EditProduct,name="editpro"),
]






