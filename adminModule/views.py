from django.http import JsonResponse
from .models import AdminModule
import json


# GET all admins / POST create admin
def admin_list(request):

    if request.method == "GET":
        admins = AdminModule.objects.all()

        data = []
        for admin in admins:
            data.append({
                "id": admin.id,
                "name": admin.name,
                "age": admin.age
            })

        return JsonResponse({
            "status": True,
            "message": "Admins fetched successfully",
            "data": data
        })


    elif request.method == "POST":
        body = json.loads(request.body)

        admin = AdminModule.objects.create(
            name=body.get("name"),
            age=body.get("age")
        )

        return JsonResponse({
            "status": True,
            "message": "Admin created successfully",
            "id": admin.id
        })

        