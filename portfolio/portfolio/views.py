from django.shortcuts import render
from .models import Contact  # Fixed import


def home(request):
    name = "harshith"
    age = 24
    return render(request, 'home.html', {
        'name': name,
        'age': age
    })


def skills(request):
    my_skills = ['python', 'java', 'git', 'django']
    return render(request, 'skills.html', {
        'skills': my_skills
    })


def contact_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']

        new_contact = Contact(  # Fixed - capital C
            name=name,
            email=email,
            number=number
        )
        new_contact.save()

        return render(request, 'complete_form.html', {
            'name': name,
            'email': email,
            'number': number,
        })
    return render(request, 'contact_form.html')

def contact_list(request):
    all_contacts=Contact.objects.all()
    return render(request, "contact_list.html", {
        'contacts' : all_contacts
    })
