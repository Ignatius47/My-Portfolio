from django.shortcuts import render
from .models import HomeSection, Developer, Resume, Service, Skill, Project, ContactInfo, Counter

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