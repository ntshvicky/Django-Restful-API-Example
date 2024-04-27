from django.http import HttpResponse, JsonResponse
def home_page(request):
    print("Home Page called!")
    data = {"message": "Hello, world. You're at the home page."}
    return JsonResponse(data)