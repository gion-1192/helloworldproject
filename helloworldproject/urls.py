from django.contrib import admin
from django.urls import path, include
from .views import helloworldfunction, HelloWorldView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', helloworldfunction),
    path('helloworld2/', HelloWorldView.as_view()),
    path('helloworldapp/', include("helloworldapp.urls"))
]
