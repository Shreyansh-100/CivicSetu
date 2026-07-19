import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def user_to_json(user):
    """
    django use to json format"""

    return {
        "id": user.id,
        "username":user.username,
    }



@csrf_exempt
@require_POST

def login_view(request):
    """
    LOGIN API
    """

    try:
        data=json.loads(request.body)
    except json.JSONDecodeError:
        
        return JsonResponse(
            {
                "ok":False,
                "error":"INVALID JSON"
                            
            },
            status=404
        )
    
    username=data.get("username","").strip()
    password=data.get("password","")

    if username =="" or password=="":
        return JsonResponse(
            {
                "ok":False,
                "error":"username or password was empty"
            },
            status=400

        )
    
    user=authenticate(
        request=request,
        username=username,
        password=password
    )

    if user is None:

        return JsonResponse(
            {
                "ok":False,
                "error":"Invalid username of password"
            },
            status=401
        )
    
    return JsonResponse(
        {
            "ok":True,
            "message":"Login Successful!!",
            "user":user_to_json(user)
        }
    )