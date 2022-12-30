from django.shortcuts import render
from .models import TeklifFormu,ServicesModel


def IndexView(request):
    services = ServicesModel.objects.all()

    context = {
        'services' : services
    }
    return render(request, 'pages/index.html', context)

def AboutView(request):
    services = ServicesModel.objects.all()

    context = {
        'services' : services
    }
    return render(request, 'pages/about.html',context)

def ContactView(request):
    services = ServicesModel.objects.all()

    context = {
        'services' : services
    }
    return render(request, 'pages/contact.html', context)

def PricingView(request):
    services = ServicesModel.objects.all()

    context = {
        'services' : services
    }
    return render(request, 'pages/pricing.html', context)

def ReferansView(request):
    services = ServicesModel.objects.all()

    context = {
        'services' : services
    }
    return render(request, 'pages/referans.html', context)

def TeklifView(request):
    if request.method == 'POST':
        name = request.POST['name']
        company = request.POST['company']
        work = request.POST['work']
        email= request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        mesaj = TeklifFormu(name=name, company=company, work=work, email=email, phone=phone, message = message)
        mesaj.save()
        return render(request, 'pages/teklif.html', {'kayit' : 'Teklifiniz başarılı bir şekilde oluşturuldu. En kısa sürede size dönüz yapılacaktır.'})

    else:
        return render(request, 'pages/teklif.html')

def ServicesView(request):
    services = ServicesModel.objects.all()

    return render(request, 'pages/services.html', {'services' : services})


def Services_Detail(request, slug):
    service = ServicesModel.objects.get(slug=slug)
    services = ServicesModel.objects.all()

    context = {
        'service' : service,
        'services' : services
    }

    return render(request, 'pages/services_detail.html', context)