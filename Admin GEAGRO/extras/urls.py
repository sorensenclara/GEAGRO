from django.urls import path
from extras.views import (
    
    # vertical
    vertical_light_sidebar_view,
    vertical_compact_sidebar_view,
    vertical_icon_sidebar_view,
    vertical_boxed_view,
    vertical_preloader_view,
    vertical_colored_sidebar_view,
    
    # horizontal
    horizontal_horizontal_view,
    horizontal_topbar_dark_view,
    horizontal_preloader_view,
    horizontal_hori_boxed_width_view,
    
    # authentication
    pages_login_view,
    pages_register_view,
    pages_recover_password_view,
    pages_lock_view,
    
    # extra-pages
    pages_timeline_view,
    pages_invoice_view,
    pages_directory_view,
    pages_blank_page_view,
    pages_error404_view,
    pages_error500_view,
)

app_name = 'extras'

urlpatterns = [

    # layouts
        # vertical
    path('layouts/vertical/light_sidebar',view=vertical_light_sidebar_view,name="layouts.vertical.light_sidebar"),
    path('layouts/vertical/compact_sidebar',view=vertical_compact_sidebar_view,name="layouts.vertical.compact_sidebar"),
    path('layouts/vertical/icont_sidebar',view=vertical_icon_sidebar_view,name="layouts.vertical.icon_sidebar"),
    path('layouts/vertical/boxed',view=vertical_boxed_view,name="layouts.vertical.boxed"),
    path('layouts/vertical/preloader',view=vertical_preloader_view,name="layouts.vertical.preloader"),
    path('layouts/vertical/colored_sidebar',view=vertical_colored_sidebar_view,name="layouts.vertical.colored_sidebar"),
    
    # horizontal
    path('layouts/horizontal/horizontal_bar',view=horizontal_horizontal_view,name="layouts.horizontal.horizontal"),
    path('layouts/horizontal/hori_topbar_dark',view=horizontal_topbar_dark_view,name="layouts.horizontal.hori_topbar_dark"),
    path('layouts/horizontal/preloader',view=horizontal_preloader_view,name="layouts.horizontal.preloader"),
    path('layouts/horizontal/hori_boxed_width',view=horizontal_hori_boxed_width_view,name="layouts.horizontal.hori_boxed_width"),
    
    
    # authentication
    path('authentication/pages_login',view=pages_login_view,name="authentication.pages_login"),
    path('authentication/register',view=pages_register_view,name="authentication.register"),
    path('authentication/recover_password',view=pages_recover_password_view,name="authentication.recover_password"),
    path('authentication/lock_screen',view=pages_lock_view,name="authentication.lock_screen"),
    
    # extra-pages
    path('extra-pages/timeline',view=pages_timeline_view,name="extra-pages.timeline"),
    path('extra-pages/invoice',view=pages_invoice_view,name="extra-pages.invoice"),
    path('extra-pages/directory',view=pages_directory_view,name="extra-pages.directory"),
    path('extra-pages/blank_page',view=pages_blank_page_view,name="extra-pages.blank_page"),
    path('extra-pages/error404',view=pages_error404_view,name="extra-pages.error404"),
    path('extra-pages/error500',view=pages_error500_view,name="extra-pages.error500"),
        
]

