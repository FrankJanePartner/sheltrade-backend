from django.urls import path
from myapp.views import supabase_auth_webhook

urlpatterns = [
    path("api/supabase/auth/", supabase_auth_webhook, name="supabase_auth_webhook"),
]
