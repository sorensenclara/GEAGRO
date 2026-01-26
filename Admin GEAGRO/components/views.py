from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ComponentsView(TemplateView):
    pass

# ui_elements
ui_elements_alerts_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-alerts.html")
ui_elements_buttons_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-buttons.html")
ui_elements_badge_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-badge.html")
ui_elements_cards_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-cards.html")
ui_elements_carousel_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-carousel.html")
ui_elements_dropdowns_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-dropdowns.html")
ui_elements_utilities_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-utilities.html")
ui_elements_grid_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-grid.html")
ui_elements_images_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-images.html")
ui_elements_lightbox_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-lightbox.html")
ui_elements_modals_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-modals.html")
ui_elements_colors_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-colors.html")
ui_elements_offcanvas_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-offcanvas.html")
ui_elements_pagination_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-pagination.html")
ui_elements_popover_tooltips_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-popover-tooltips.html")
ui_elements_rangeslider_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-rangeslider.html")
ui_elements_session_timeout_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-session-timeout.html")
ui_elements_progressbars_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-progressbars.html")
ui_elements_sweet_alert_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-sweet-alert.html")
ui_elements_tabs_accordions_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-tabs-accordions.html")
ui_elements_typography_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-typography.html")
ui_elements_video_view = ComponentsView.as_view(template_name = "components/ui-elements/ui-video.html")

# forms
forms_elements_view = ComponentsView.as_view(template_name = "components/forms/form-elements.html")
forms_validation_view = ComponentsView.as_view(template_name = "components/forms/form-validation.html")
forms_advanced_view = ComponentsView.as_view(template_name = "components/forms/form-advanced.html")
forms_editors_view = ComponentsView.as_view(template_name = "components/forms/form-editors.html")
forms_uploads_view = ComponentsView.as_view(template_name = "components/forms/form-uploads.html")
forms_xeditable_view = ComponentsView.as_view(template_name = "components/forms/form-xeditable.html")

# charts
charts_morris_view = ComponentsView.as_view(template_name = "components/charts/charts-morris.html")
charts_chartist_view = ComponentsView.as_view(template_name = "components/charts/charts-chartist.html")
charts_chartjs_view = ComponentsView.as_view(template_name = "components/charts/charts-chartjs.html")
charts_flot_view = ComponentsView.as_view(template_name = "components/charts/charts-flot.html")
charts_c3_view = ComponentsView.as_view(template_name = "components/charts/charts-c3.html")
charts_other_view = ComponentsView.as_view(template_name = "components/charts/charts-other.html")

# tables
tables_basic_view = ComponentsView.as_view(template_name = "components/tables/tables-basic.html")
tables_datatable_view = ComponentsView.as_view(template_name = "components/tables/tables-datatable.html")
tables_responsive_view = ComponentsView.as_view(template_name = "components/tables/tables-responsive.html")
tables_editable_view = ComponentsView.as_view(template_name = "components/tables/tables-editable.html")

# icons
icons_material_view = ComponentsView.as_view(template_name = "components/icons/icons-material.html")
icons_ion_view = ComponentsView.as_view(template_name = "components/icons/icons-ion.html")
icons_fontawesome_view = ComponentsView.as_view(template_name = "components/icons/icons-fontawesome.html")
icons_themify_view = ComponentsView.as_view(template_name = "components/icons/icons-themify.html")
icons_dripicons_view = ComponentsView.as_view(template_name = "components/icons/icons-dripicons.html")
icons_typicons_view = ComponentsView.as_view(template_name = "components/icons/icons-typicons.html")

# maps
maps_google_view = ComponentsView.as_view(template_name = "components/maps/maps-google.html")
maps_vector_view = ComponentsView.as_view(template_name = "components/maps/maps-vector.html")


    
    
