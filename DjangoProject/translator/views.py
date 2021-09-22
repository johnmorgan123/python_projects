from django.shortcuts import render


# Create your views here.

def translator_view(request):
    if request.methods == 'POST':
        origional_text = request.POST['my_textarea']
    else:
        return render(request, 'translator.html')
