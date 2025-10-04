import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

@csrf_exempt
def supabase_auth_webhook(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        event_type = data.get("type")
        record = data.get("record", {})

        email = record.get("email")
        user_id = record.get("id")

        if event_type == "INSERT" and email:
            # Create Django user if not exists
            User.objects.get_or_create(
                username=email,
                email=email,
                defaults={"is_active": True}
            )

        elif event_type == "DELETE" and email:
            # Optionally delete Django user
            User.objects.filter(email=email).delete()

        return JsonResponse({"status": "success"})

    return JsonResponse({"error": "invalid method"}, status=405)
