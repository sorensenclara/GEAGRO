from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ExtrasView(TemplateView):
    pass

# layouts
    # vertical
vertical_light_sidebar_view = ExtrasView.as_view(template_name = "extras/layouts/vertical/layouts-light-sidebar.html")
vertical_compact_sidebar_view = ExtrasView.as_view(template_name = "extras/layouts/vertical/layouts-compact-sidebar.html")
vertical_icon_sidebar_view = ExtrasView.as_view(template_name = "extras/layouts/vertical/layouts-icon-sidebar.html")
vertical_boxed_view = ExtrasView.as_view(template_name = "extras/layouts/vertical/layouts-boxed.html")
vertical_preloader_view = ExtrasView.as_view(template_name = "extras/layouts/vertical/layouts-preloader.html")
vertical_colored_sidebar_view = ExtrasView.as_view(template_name = "extras/layouts/vertical/layouts-colored-sidebar.html")

    # horizontal
horizontal_horizontal_view = ExtrasView.as_view(template_name = "extras/layouts/horizontal/layouts-horizontal.html")
horizontal_topbar_dark_view = ExtrasView.as_view(template_name = "extras/layouts/horizontal/layouts-hori-topbar-dark.html")
horizontal_preloader_view = ExtrasView.as_view(template_name = "extras/layouts/horizontal/layouts-hori-preloader.html")
horizontal_hori_boxed_width_view = ExtrasView.as_view(template_name = "extras/layouts/horizontal/layouts-hori-boxed-width.html")
    
    
# authentication 
pages_login_view = ExtrasView.as_view(template_name = "extras/authentication/pages-login.html")
pages_register_view = ExtrasView.as_view(template_name = "extras/authentication/pages-register.html")
pages_recover_password_view = ExtrasView.as_view(template_name = "extras/authentication/pages-recoverpw.html")
pages_lock_view = ExtrasView.as_view(template_name = "extras/authentication/pages-lock-screen.html")
 
#  extra-pages
pages_timeline_view = ExtrasView.as_view(template_name = "extras/extra-pages/pages-timeline.html")
pages_invoice_view = ExtrasView.as_view(template_name = "extras/extra-pages/pages-invoice.html")
pages_directory_view = ExtrasView.as_view(template_name = "extras/extra-pages/pages-directory.html")
pages_blank_page_view = ExtrasView.as_view(template_name = "extras/extra-pages/pages-blank.html")
pages_error404_view = ExtrasView.as_view(template_name = "extras/extra-pages/pages-404.html")
pages_error500_view = ExtrasView.as_view(template_name = "extras/extra-pages/pages-500.html")
