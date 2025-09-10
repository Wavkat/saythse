from django.shortcuts import render
from .models import Contact
from django.http import JsonResponse

def home(request):
    qidiruv = request.GET.get('q', '')
    contacts = []
    contacts = Contact.objects.all()

    if qidiruv.isdigit():
        contacts = Contact.objects.filter(auto_number=int(qidiruv))

    return render(request, 'home.html', {'contacts': contacts, 'qidiruv': qidiruv})


def ajax_search(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        contacts = Contact.objects.filter(number__icontains=query)
        for c in contacts:
            results.append({
                'number': c.number,
                'name': c.name,
                'Job': c.Job,
            })
    return JsonResponse({'results': results})