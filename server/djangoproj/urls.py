from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django admin
    path(
        "admin/",
        admin.site.urls,
    ),

    # React frontend routes (SPA)
    path(
        "",
        TemplateView.as_view(
            template_name="index.html",
        ),
    ),
    path(
        "dealers/",
        TemplateView.as_view(
            template_name="index.html",
        ),
    ),
    path(
        "dealer/<int:dealer_id>",
        TemplateView.as_view(
            template_name="index.html",
        ),
    ),
    path(
        "login/",
        TemplateView.as_view(
            template_name="index.html",
        ),
    ),
    path(
        "register/",
        TemplateView.as_view(
            template_name="index.html",
        ),
    ),
    path(
        "postreview/<int:dealer_id>",
        TemplateView.as_view(
            template_name="index.html",
        ),
    ),

    # Django backend APIs
    path(
        "djangoapp/",
        include("djangoapp.urls"),
    ),
]

# Static & media files
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT,
)
