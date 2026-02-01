from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # React routes (IMPORTANT)
    path('login/', TemplateView.as_view(template_name="index.html")),
    path('register/', TemplateView.as_view(template_name="index.html")),
    path('dealers/', TemplateView.as_view(template_name="index.html")),
    path('dealer/<int:dealer_id>', TemplateView.as_view(template_name="index.html")),
    path('postreview/<int:dealer_id>', TemplateView.as_view(template_name="index.html")),

    # Django backend APIs
    path('djangoapp/', include('djangoapp.urls')),
]
