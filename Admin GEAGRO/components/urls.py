from django.urls import path
from components.views import (
    
    ui_elements_alerts_view,
    ui_elements_buttons_view,
    ui_elements_badge_view,
    ui_elements_cards_view,
    ui_elements_carousel_view,
    ui_elements_dropdowns_view,
    ui_elements_utilities_view,
    ui_elements_grid_view,
    ui_elements_images_view,
    ui_elements_lightbox_view,
    ui_elements_modals_view,
    ui_elements_colors_view,
    ui_elements_offcanvas_view,
    ui_elements_pagination_view,
    ui_elements_popover_tooltips_view,
    ui_elements_rangeslider_view,
    ui_elements_session_timeout_view,
    ui_elements_progressbars_view,
    ui_elements_sweet_alert_view,
    ui_elements_tabs_accordions_view,
    ui_elements_typography_view,
    ui_elements_video_view,
    
    # forms
    forms_elements_view,
    forms_validation_view,
    forms_advanced_view,
    forms_editors_view,
    forms_uploads_view,
    forms_xeditable_view,
    
    # charts
    charts_morris_view,
    charts_chartist_view,
    charts_chartjs_view,
    charts_flot_view,
    charts_c3_view,
    charts_other_view,
    
    # tables
    tables_basic_view,
    tables_datatable_view,
    tables_responsive_view,
    tables_editable_view,

    # icons
    icons_material_view,
    icons_ion_view,
    icons_fontawesome_view,
    icons_themify_view,
    icons_dripicons_view,
    icons_typicons_view,
    
    # maps
    maps_google_view,
    maps_vector_view,
    
)

app_name = 'components'

urlpatterns = [
    
    # ui-elements
    path('ui_elements/alerts',view=ui_elements_alerts_view,name="ui-elements.alerts"),
    path('ui_elements/buttons',view=ui_elements_buttons_view,name="ui-elements.buttons"),
    path('ui_elements/badge',view=ui_elements_badge_view,name="ui-elements.badge"),
    path('ui_elements/cards',view=ui_elements_cards_view,name="ui-elements.cards"),
    path('ui_elements/carousel',view=ui_elements_carousel_view,name="ui-elements.carousel"),
    path('ui_elements/dropdowns',view=ui_elements_dropdowns_view,name="ui-elements.dropdowns"),
    path('ui_elements/utilities',view=ui_elements_utilities_view,name="ui-elements.utilities"),
    path('ui_elements/grid',view=ui_elements_grid_view,name="ui-elements.grid"),
    path('ui_elements/images',view=ui_elements_images_view,name="ui-elements.images"),
    path('ui_elements/lightbox',view=ui_elements_lightbox_view,name="ui-elements.lightbox"),
    path('ui_elements/modals',view=ui_elements_modals_view,name="ui-elements.modals"),
    path('ui_elements/colors',view=ui_elements_colors_view,name="ui-elements.colors"),
    path('ui_elements/offcanvas',view=ui_elements_offcanvas_view,name="ui-elements.offcanvas"),
    path('ui_elements/pagination',view=ui_elements_pagination_view,name="ui-elements.pagination"),
    path('ui_elements/popover_tooltips',view=ui_elements_popover_tooltips_view,name="ui-elements.popover_tooltips"),
    path('ui_elements/rangeslider',view=ui_elements_rangeslider_view,name="ui-elements.rangeslider"),
    path('ui_elements/session_timeout',view=ui_elements_session_timeout_view,name="ui-elements.session_timeout"),
    path('ui_elements/progressbars',view=ui_elements_progressbars_view,name="ui-elements.progressbars"),
    path('ui_elements/sweet_alert',view=ui_elements_sweet_alert_view,name="ui-elements.sweet_alert"),
    path('ui_elements/tabs_accordions',view=ui_elements_tabs_accordions_view,name="ui-elements.tabs_accordions"),
    path('ui_elements/typography',view=ui_elements_typography_view,name="ui-elements.typography"),
    path('ui_elements/video',view=ui_elements_video_view,name="ui-elements.video"),
    
    # forms
    path('forms/elements',view=forms_elements_view,name="forms.elements"),
    path('forms/validation',view=forms_validation_view,name="forms.validation"),
    path('forms/advanced',view=forms_advanced_view,name="forms.advanced"),
    path('forms/editors',view=forms_editors_view,name="forms.editors"),
    path('forms/uploads',view=forms_uploads_view,name="forms.uploads"),
    path('forms/xeditable',view=forms_xeditable_view,name="forms.xeditable"),
    
    # charts
    path('charts/morris',view=charts_morris_view,name="charts.morris"),
    path('charts/chartist',view=charts_chartist_view,name="charts.chartist"),
    path('charts/chartjs',view=charts_chartjs_view,name="charts.chartjs"),
    path('charts/flot',view=charts_flot_view,name="charts.flot"),
    path('charts/c3',view=charts_c3_view,name="charts.c3"),
    path('charts/other',view=charts_other_view,name="charts.other"),
    
    # tables
    path('tables/basic',view=tables_basic_view,name="tables.basic"),
    path('tables/datatable',view=tables_datatable_view,name="tables.datatable"),
    path('tables/responsive',view=tables_responsive_view,name="tables.responsive"),
    path('tables/editable',view=tables_editable_view,name="tables.editable"),
 
    # icons
    path('icons/material',view=icons_material_view,name="icons.material"),
    path('icons/ion',view=icons_ion_view,name="icons.ion"),
    path('icons/fontawesome',view=icons_fontawesome_view,name="icons.fontawesome"),
    path('icons/themify',view=icons_themify_view,name="icons.themify"),
    path('icons/dripicons',view=icons_dripicons_view,name="icons.dripicons"),
    path('icons/typicons',view=icons_typicons_view,name="icons.typicons"),
 
    # maps
    path('maps/google',view=maps_google_view,name="maps.google"),
    path('maps/vector',view=maps_vector_view,name="maps.vector"),
       
   
    
]