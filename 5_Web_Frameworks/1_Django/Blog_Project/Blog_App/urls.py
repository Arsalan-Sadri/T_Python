from django.urls import path
from . import views 

# This urlpatterns gets passed as an arg to include() function
# in <project_root>.urls 
urlpatterns = [
    path("", views.home, name="blog-home"),
    path("about", views.about, name="blog-about")
]
