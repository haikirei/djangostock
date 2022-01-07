from django.shortcuts import render

def home(request):
    import requests
    import json
    # pk_ebfa12885d9f421fbc30a04d37231325
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_ebfa12885d9f421fbc30a04d37231325")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error"
    return render(request, 'home.html', {'api':api})

def about(request):
    return render(request, 'about.html', {})