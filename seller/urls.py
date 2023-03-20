from .views import *
from django.urls import path


urlpatterns = [
    path('seller_blank_pages/', seller_blank_pages, name='seller_blank_pages'),
    path('seller_bootstrap_alert/', seller_bootstrap_alert,name='seller_bootstrap_alert'),
    path('seller_bootstrap_badge/',seller_bootstrap_badge,name='seller_bootstrap_badge'),
    path('seller_bootstrap_breadcrumb/',seller_bootstrap_breadcrumb,name='seller_bootstrap_breadcrumb'),
    path('seller_bootstrap_card/',seller_bootstrap_card,name='seller_bootstrap_card'),
    path('seller_bootstrap_carousel/',seller_bootstrap_carousel,name='seller_bootstrap_carousel'),
    path('seller_bootstrap_dropdown/',seller_bootstrap_dropdown,name='seller_bootstrap_dropdown'),
    path('seller_bootstrap_list_group/',seller_bootstrap_list_group,name='seller_bootstrap_list_group'),
    path('seller_bootstrap_modal/',seller_bootstrap_modal,name='seller_bootstrap_modal'),
    path('seller_bootstrap_nav/',seller_bootstrap_nav,name='seller_bootstrap_nav'),
    path('seller_bootstrap_pagination/',seller_bootstrap_pagination,name='seller_bootstrap_pagination'),
    path('seller_bootstrap_progress/',seller_bootstrap_progress,name='seller_bootstrap_progress'),
    path('seller_bootstrap_spinner/',seller_bootstrap_spinner,name='seller_bootstrap_spinner'),
    path('seller_buttons/',seller_buttons,name='seller_buttons'),
    path('seller_chart_apexcharts/',seller_chart_apexcharts,name='seller_chart_apexcharts'),
    path('seller_chart_chartjs/',seller_chart_chartjs,name='seller_chart_chartjs'),
    path('seller_chatboxs/',seller_chatboxs,name='seller_chatboxs'),
    path('seller_component_avatar/',seller_component_avatar,name='seller_component_avatar'),
    path('seller_component_hero/',seller_component_hero,name='seller_component_hero'),
    path('seller_component_sweet_alert/',seller_component_sweet_alert,name='seller_component_sweet_alert'),
    path('seller_component_toastify/',seller_component_toastify,name='seller_component_toastify'),
    path('seller_credits/',seller_credits,name='seller_credits'),
    path('seller_default/',seller_default,name='seller_default'),
    path('seller_layout_top_navigation/',seller_layout_top_navigation,name='seller_layout_top_navigation'),
    path('seller_editor/',seller_editor,name='seller_editor'),
    path('seller_email/',seller_email,name='seller_email'),
    path('seller_errors_403/',seller_errors_403,name='seller_errors_403'),
    path('seller_errors_404/',seller_errors_404,name='seller_errors_404'),
    path('seller_errors_500/',seller_errors_500,name='seller_errors_500'),
    path('seller_errors_503/',seller_errors_503,name='seller_errors_503'),
    path('seller_forgot_password/',seller_forgot_password,name='seller_forgot_password'),
    path('seller_forms_checkbox/',seller_forms_checkbox,name='seller_forms_checkbox'),
    path('seller_icons_boostrap/',seller_icons_boostrap,name='seller_icons_boostrap'),
    path('seller_index/',seller_index,name='seller_index'),
    path('seller_pricing/',seller_pricing,name='seller_pricing'),
    path('seller_profile/',seller_profile,name='seller_profile'),
    path('seller_radio/',seller_radio,name='seller_radio'),
    path('seller_register/',seller_register,name='seller_register'),
    path('seller_reset_password/',seller_reset_password,name='seller_reset_password'),
    path('seller_header/',seller_header,name='seller_header'),
    path('seller_forms_validation/',seller_forms_validation,name='seller_forms_validation'),
    path('seller_widgets_email/',seller_widgets_email,name='seller_widgets_email'),
    path('seller_login/',seller_login,name='seller_login'),
    path('seller_logout/',seller_logout,name='seller_logout'),
    path('seller_add_product/',seller_add_product,name='seller_add_product'),
    path('seller_otp/' ,seller_otp, name='seller_otp' ),
    path('my_product/' ,my_product, name='my_product' ),
    path('product_edit/<int:pk>' ,product_edit, name='product_edit' ),
    path('product_delete/<int:pk>' ,product_delete, name='product_delete' ),
  



   
  



]