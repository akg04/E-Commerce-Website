from django.urls import path
from . import views
urlpatterns = [
    #yaha mac urls.py se aayega aur shop/ k baad blank dekhkar wo view.index pe jayega
    path("",views.index,name="blogHome"),
    path("bloggpost/<int:id>", views.bloggpost, name="blogPost")

]