# from django.shortcuts import render
# import requests

# def index(request):
#     if request.method == 'POST':
#         name = request.POST.get("name")
#         api_url = f'http://127.0.0.1:8000/marks/{name}'  # Replace with your API endpoint URL
#         response = requests.get(api_url)
#         student_data = response.json()
#         if response.status_code == 200:
#             menu_data = response.json()
#             return render(request, 'results.html', {'student_data': menu_data})
#         else:
#             return render(request, 'index.html', {'message': 'Failed to fetch student results. Check Again!'})
    
        
#     return render(request, 'index.html')

from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        api_url = f'http://127.0.0.1:8000/menu/{name}'  # Replace with your API endpoint URL
        response = requests.get(api_url)
        if response.status_code == 200:
            menu_data = response.json()
            return render(request, 'results.html', {'menu_data':menu_data})
        else:
            return render(request, 'index.html', {'message': 'Failed to fetch student results. Check Again!'})
    
    return render(request, 'index.html')



