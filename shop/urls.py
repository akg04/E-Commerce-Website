from django.urls import path
#migrate table banaata h
from . import views
urlpatterns = [
    #yaha mac urls.py se aayega aur shop/ k baad blank dekhkar wo view.index pe jayega
    path("",views.index,name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/",views.checkout,name="Checkout"),
    path("handlerequest/", views.handlerequest, name="handleRequest"),

]