from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class DashboardView(LoginRequiredMixin,TemplateView):
    pass

dashboard_view = DashboardView.as_view(template_name = "dashboard/index.html")
calendar_view = DashboardView.as_view(template_name = "dashboard/calendar.html")

# email
email_inbox_view = DashboardView.as_view(template_name = "dashboard/email/email-inbox.html")
email_compose_view = DashboardView.as_view(template_name = "dashboard/email/email-compose.html")
email_read_view = DashboardView.as_view(template_name = "dashboard/email/email-read.html")

chat_view = DashboardView.as_view(template_name = "dashboard/chat.html")
kanbanboard_view = DashboardView.as_view(template_name = "dashboard/kanbanboard.html")
