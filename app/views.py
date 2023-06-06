from django.shortcuts import render
from .models import ProfileData, Tool, SocialLink


def home(request):
    profile = ProfileData.objects.first()
    tools = Tool.objects.all().order_by("order")
    social_links = SocialLink.objects.all().order_by('order')

    context = {
        "profile": profile,  # object
        "tools": tools,  # queryset (list)
        "social_links": social_links
    }

    return render(request, "index.html", context)
