from django.shortcuts import render

def hello(request):
    if request.method == 'POST':
        selected_option = request.POST['dropdown']
        return render(request, 'index.html', {'selected_option': selected_option})
    return render(request, 'index.html')
