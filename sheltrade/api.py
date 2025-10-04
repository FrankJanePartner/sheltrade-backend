from django.http import JsonResponse
from .auth_utils import verify_supabase_jwt

def protected_view(request):
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    payload = verify_supabase_jwt(token)
    if not payload:
        return JsonResponse({"error": "Unauthorized"}, status=401)

    email = payload.get("email")
    return JsonResponse({"message": f"Welcome, {email}!"})
