from django.shortcuts import render

def home_view(request):
    if request.user.is_authenticated:
        context = {
            'isim': 'Erdem',
            'soyisim': 'Demirkapı',
        }
    else:
         context = {
            'isim': 'Guest',
            'soyisim': '',
        }

    return render(request, 'home.html', context )