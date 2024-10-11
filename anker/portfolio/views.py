from django.shortcuts import render
from .models import HomeSection, Developer, Resume, Service, Skill, Project, ContactInfo, Counter
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Function-based view to render the portfolio's index.html with all sections.
def index(request):
    # Fetch data from models for each section.
    
    # Home Section (greeting, name, title, etc.)
    home = HomeSection.objects.first()
    
    # About Section (developer details)
    developer = Developer.objects.first()
    
    # Resume Section (bio and CV)
    resume = Resume.objects.first() 
    
    # Services Section (list of services offered)
    services = Service.objects.all()
    
    # Skills Section (skills and their proficiency)
    skills = Skill.objects.all()
    
    # Projects Section (portfolio projects)
    projects = Project.objects.all()
    
    # Contact Info Section (contact details like email, phone, etc.)
    contact_info = ContactInfo.objects.all()
    
    # Counter Section (stats like completed projects, years of experience, etc.)
    counters = Counter.objects.all()

    # Context to be passed to the template
    context = {
        'home': home,
        'developer': developer,
        'resume': resume,
        'services': services,
        'skills': skills,
        'projects': projects,
        'contact_info': contact_info,
        'counters': counters,
    }

    # Render the 'index.html' template with the above context.
    return render(request, 'portfolio/index.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_massage = f"Message from {name} ({email}):\n\n{message}"
            send_mail(
                subject,
                full_massage,

'your_gmail_account@gmail.com',
['ignatiusx47@gmail.com'],
            )
            return JsonResponse({'success': 'Your message has been sent successfully!'})
        else:
            return JsonResponse({'error': 'All fields are required.'}, status=400)
    
    return JsonResponse({'error': 'Invalid request method.'}, status=400)