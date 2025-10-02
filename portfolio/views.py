from django.shortcuts import render, redirect

# Importing my Models
from .models import Email, Project, Skill, Service, SuccessStory, AboutWork, Achievement, HeadingText, ExtraText, Logos, Biography, SocialLink

# Importing Email Form
from . forms import EmailForm

# Create your views here.
def index(request):

    form = EmailForm()


    # Getting my model data
    projects = Project.objects.all()
    biography = Biography.objects.first()
    main_heading = HeadingText.objects.first()
    services = Service.objects.all()
    logos = Logos.objects.all()
    skils = Skill.objects.all()
    social_links = SocialLink.objects.all()[:4] # Get the first 4 social links
    footer_social_links = SocialLink.objects.all()[4:] # Get the remaining social links
    success_stories = SuccessStory.objects.all()
    success_story_text = ExtraText.objects.last()
    services_text = ExtraText.objects.first()
    about_work = AboutWork.objects.all()
    achievements = Achievement.objects.all()

    context = {
        'form': form,
        'projects': projects,
        'biography': biography,
        'main_heading': main_heading,
        'services': services,
        'logos': logos,
        'skills': skils,
        'social_links': social_links,
        'footer_social_links': footer_social_links,
        'success_stories': success_stories,
        'success_story_text': success_story_text,
        'services_text': services_text,
        'about_work': about_work,
        'achievements': achievements,
    }

    if (request.method == 'POST'):

        # Validating Email and input data
        form = EmailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            mail_data = Email.objects.create(name=name, email=email, message=message)
            mail_data.save()

            return redirect('index'),  # Redirect to the same page to show the success message
    
    return render(request, 'portfolio/index.html', context=context)