from django.views.generic import RedirectView

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

from .views import MyPasswordChangeView, MyPasswordSetView


urlpatterns = [
    # =========================
    # Admin
    # =========================
    path("admin/", admin.site.urls),

    # =========================
    # Dashboard (GEAGRO / Lexa)
    # =========================
    path("dashboard/", include("dashboard.urls")),

    # =========================
    # Components (UI)
    # =========================
    path("components/", include("components.urls")),

    # =========================
    # Extras (layouts, auth demo, error pages)
    # =========================
    path("extras/", include("extras.urls")),

    # =========================
    # Account / Auth
    # =========================
    path(
        "account/password/change/",
        login_required(MyPasswordChangeView.as_view()),
        name="account_change_password",
    ),
    path(
        "account/password/set/",
        login_required(MyPasswordSetView.as_view()),
        name="account_set_password",
    ),
    path("account/", include("allauth.urls")),

    path("", RedirectView.as_view(url="/dashboard/", permanent=False)),
]

# =========================
# Static files (dev only)
# =========================
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)


