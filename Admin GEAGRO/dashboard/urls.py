from django.urls import path
from dashboard.views import (
    
    dashboard_view,
    calendar_view,
    weather_view,
    alert_view,
    wines_view,

    
    email_inbox_view,
    email_compose_view,
    email_read_view,
    
    chat_view,
    kanbanboard_view,
)

app_name = 'dashboard'

urlpatterns = [
    
    path('',view=dashboard_view,name="dashboard"),
    path('calendar',view=calendar_view,name="calendar"),

    path('weather',view=weather_view,name="weather"),
    path('weather',view=alert_view,name="alert"),
    path('weather',view=wines_view,name="wines"),
    
    # email
    path('email/email_inbox',view=email_inbox_view,name="email.email_inbox"),
    path('email/email_compose',view=email_compose_view,name="email.email_compose"),
    path('email/email_read',view=email_read_view,name="email.email_read"),
    
    path('chat',view=chat_view,name="chat"),
    path('kanbanboard',view=kanbanboard_view,name="kanbanboard"),
    
]

