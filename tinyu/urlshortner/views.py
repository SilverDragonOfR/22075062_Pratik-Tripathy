from django.shortcuts import render, redirect
from .models import URL
from django.http import HttpResponse, HttpResponseNotFound
import json
import uuid

# Helper functions

def generate_short_url_from_long_url(long_url):
    all_short_urls = URL.objects.values("short_url")
    new_short_url = str(uuid.uuid4())[:8]
    while new_short_url in all_short_urls:
        new_short_url = uuid.uuid4()[:8]
    return new_short_url

# Create your views here.

def index(request):
    return render(request, "index.html")

def list(request):
    qs = URL.objects.all()
    query = {"data": []}
    for q in qs: query["data"].append({"short_url": q.short_url, "long_url": q.long_url})
    return render(request, "list.html", query)

def create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        long_url = data["longURL"]
        short_url = generate_short_url_from_long_url(long_url=long_url)
        new_url = URL(short_url=short_url, long_url=long_url)
        new_url.save()
        return HttpResponse(json.dumps({
            "success" : True,
            "shortURL": f'http://localhost:8000/find/{short_url}'
        }), status=200)
    else:
        return HttpResponseNotFound("Page not found", status=404)
    
def go(request, shortURL):
    print(shortURL)
    url = URL.objects.get(short_url=shortURL)
    return redirect(url.long_url)