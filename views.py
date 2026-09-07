import json

from django.contrib.auth import authenticate, get_user_model, login, logout

# from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.http import require_http_methods

User = get_user_model()


@require_http_methods(["POST"])
def login_view(request):
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user, backend="django.contrib.auth.backends.ModelBackend")
        # Return success response with username
        return JsonResponse({"success": True, "username": username})
    else:
        # Return an 'invalid login' error message
        return JsonResponse({"error": "invalid credentials"}, status=401)


@require_http_methods(["POST"])
def logout_view(request):
    logout(request)
    return JsonResponse({"success": True, "message": "logged out successfully"})


@require_http_methods(["GET"])
def user_view(request):
    if request.user.is_authenticated:
        user = request.user
        return JsonResponse(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }
        )
    else:
        return JsonResponse({"error": "user not logged in"}, status=401)


@require_http_methods(["POST"])
def register_view(request):
    data = json.loads(request.body)
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # validate password
    try:
        validate_password(password)
    except ValidationError as e:
        return JsonResponse({"error": e.messages}, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({"error": "email is already taken"}, status=400)
    else:
        user = User.objects.create_user(username, email, password)
        login(request, user, backend="django.contrib.auth.backends.ModelBackend")
        return JsonResponse(
            {
                "success": True,
            }
        )


@require_http_methods(["GET"])
def get_csrf(request):
    get_token(request)  # force Django to set CSRF token
    return JsonResponse(
        {
            "success": True,
        }
    )
