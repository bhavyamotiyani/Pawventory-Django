from django.shortcuts import render

def about_page(request):
    return render(request, 'pages/about.html')
