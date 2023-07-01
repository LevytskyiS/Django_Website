from django.shortcuts import render


# Create your views here.
def index(request):
    data = {
        "title": "Main page",
        "values": ["Some", "Hello", "Bye"],
        "obj": {"car": "BMW", "age": 10, "hobby": "Football"},
    }
    return render(request, "main/index.html", data)


def about(request):
    return render(request, "main/about.html")
