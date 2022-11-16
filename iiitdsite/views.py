from unicodedata import category
from django.views.generic import ListView,DetailView, TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import Faculty, Images,Magazine_Issues, Magazine_Team, NewsLetterEmail, Events, EventsImages, About, AboutUsTestimonial, Tenders, Updates, Gallery_categories
from .models import OurFamilyLink, AcademicsECE, AcademicsCSE, AcademicsDSAI, Academics, ResearchPoints, ResearchStudents
from .models import CurriculumLink, NewsPage, AcademicCalLink, HomePageUpcomingEvents, Administration, Staff, Senate, Financial_Committee,BOG 
from .models import ugcselinks, phdlinks, Scholarship, Alert, Placements, HomePageGallery, Jobs,Announcements, Gallery, CampusPageDetails, Clubs
from .weather import temp_cel, temp_fah
UserModel = get_user_model()


def home(request):
    alert = Alert.objects.last()
    announcements=Announcements.objects.all()[::-1]
    updates=Updates.objects.all()[::-1]
    links = ugcselinks.objects.last()
    events = Events.objects.all()[::-1]
    main_event = Events.objects.last()
    upcoming_events = HomePageUpcomingEvents.objects.all()[::-1]
    acad_link = AcademicCalLink.objects.get(id=1)
    main_news = NewsPage.objects.last()
    news = NewsPage.objects.all()[2:6:-1]
    currilink = CurriculumLink.objects.get(id=1)
    gallery = HomePageGallery.objects.all()[::-1]
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('')
    return render(request, 'iiitdsite/index.html', {'alert': alert, 'main_event': main_event, 'events': events,
                                                    'gallery': gallery, 'images': EventsImages, 'upcoming_events': upcoming_events, 'main_news': main_news, 'acad_link': acad_link, 'news': news, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,'announcements':announcements,'updates':updates})



def faculty(request):
    members = Faculty.objects.all()
    return render(request, 'iiitdsite/faculty.html', {'members':members})




def aboutus(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    about = About.objects.all()
    ourfam = OurFamilyLink.objects.all()
    testi = AboutUsTestimonial.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/about')
    return render(request, 'iiitdsite/about_us.html', {'acad_link': acad_link, 'currilink': currilink,'about': about, 'ourfam': ourfam,
                                                       'testi': testi,'temp_cel': temp_cel,
                                                       'temp_fah': temp_fah, 'links': links,})





def academicscse(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    acadcse = AcademicsCSE.objects.all()
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/academics-cse')
    return render(request, 'iiitdsite/acad_cse.html', {'acad_link': acad_link, 'currilink': currilink,'acadcse': acadcse, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})




def academicsece(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    acadece = AcademicsECE.objects.all()
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/academics-ece')
    return render(request, 'iiitdsite/acad_ece.html', {'acad_link': acad_link, 'currilink': currilink,'acadece': acadece, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})



def academicsdsai(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    acaddsai = AcademicsDSAI.objects.all()
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/academics-dsai')
    return render(request, 'iiitdsite/acad_dsai.html', {'acad_link': acad_link, 'currilink': currilink,'acaddsai': acaddsai, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})



def academics(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    academics = Academics.objects.all()
    currilink = CurriculumLink.objects.get(id=1)
    students = ResearchStudents.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/academics')
    return render(request, 'iiitdsite/academics.html', {'acad_link': acad_link, 'currilink': currilink,'academics': academics, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,'students':students})




def contact(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/contact')
    return render(request, 'iiitdsite/contact.html', {'acad_link': acad_link, 'currilink': currilink,'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})




# def gallery(request):
#     links = ugcselinks.objects.last()
#     acad_link = AcademicCalLink.objects.get(id=1)
#     currilink = CurriculumLink.objects.get(id=1)
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         emailid = NewsLetterEmail.objects.create(email_id=email)
#         NewsLetterEmail.save(emailid)
#         return redirect('/gallery')
#     list = Events.objects.all()[::-1]
#     images = Gallery.objects.all()
#     return render(request, 'iiitdsite/gallery.html', {'acad_link': acad_link, 'currilink': currilink, 'list': list,
#                                                       'EventsImages': EventsImages, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,'images': images})




def jobs(request):
    job_links = Jobs.objects.last()
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/jobs')
    return render(request, 'iiitdsite/jobs.html', {'job_links': job_links, 'acad_link': acad_link, 'currilink': currilink,'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})




def newstack(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    num = NewsPage.objects.count()
    main_news = NewsPage.objects.last()
    news = NewsPage.objects.all()[:num-1:-1]
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/newstack')
    return render(request, 'iiitdsite/newstack.html', {'acad_link': acad_link, 'main_news': main_news, 'news': news, 'currilink': currilink,'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})




def placements(request):
    companies_active = Placements.objects.all()[0:4]
    companies = Placements.objects.all()[4:]
    lst = len(companies)
    if lst%4 == 0:
        iters = range(1, (lst//4)+1)
    elif lst%4 != 0:
        iters = range(1, (lst//4)+2)
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/placements')
    return render(request, 'iiitdsite/placements.html', {'lst': lst, 'iters': iters, 'companies': companies, 'companies_active': companies_active, 'acad_link': acad_link, 'currilink': currilink,'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})




def research(request):
    students = ResearchStudents.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/research')
    return render(request, 'iiitdsite/research.html', { 'students': students,})




def administration(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    administration = Administration.objects.all()[::-1]
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/administration')
    return render(request, 'iiitdsite/administration.html', {'administration': administration, 'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})




def admissions(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/admissions')
    return render(request, 'iiitdsite/admission.html', {'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})



def staff(request):
    members= Staff.objects.all()
    return render(request, 'iiitdsite/staff.html', {'members': members})




def ugcse(request):
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    links = ugcselinks.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/ug-cse')
    return render(request, 'iiitdsite/undergraduate_cse.html',
                  {'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel,
                   'temp_fah': temp_fah, 'links': links})





def phd(request):
    links = phdlinks.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/phd')
    return render(request, 'iiitdsite/Phd.html',
                  {
                    'links': links})




def faqs(request):
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/faq')
    return render(request, 'iiitdsite/FAQ.html',
                  {'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel,
                   'temp_fah': temp_fah})




def Scholarships(request):
    links = Scholarship.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/scholarship')
    return render(request, 'iiitdsite/scholarship.html',
                  {'links': links, 'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel,
                   'temp_fah': temp_fah})




def chatbot(request):
    return render(request, 'iiitdsite/chatbot_abd.html')


def campus(request):
    house = CampusPageDetails.objects.get(id=1)
    labs = CampusPageDetails.objects.get(id=2)
    sports = CampusPageDetails.objects.get(id=3)
    arts = CampusPageDetails.objects.get(id=4)
    health = CampusPageDetails.objects.get(id=5)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/campus')
    return render(request, 'iiitdsite/campus.html', {'house': house, 'sports': sports, 'labs': labs, 'health': health,
                                                     'arts': arts, 'temp_cel': temp_cel, 'temp_fah': temp_fah})



def magazine(request):
    issues = Magazine_Issues.objects.all()[::-1]
    return render(request, 'iiitdsite/magazine.html', {'issues':issues})

def magazine_team(request):
    membersCS = Magazine_Team.objects.filter(tag="Content Support")
    membersEditor = Magazine_Team.objects.filter(tag="Faculty")
    membersDesign = Magazine_Team.objects.filter(tag="Design")
    membersMC = Magazine_Team.objects.filter(tag="Magazine Coordinator")
    return render(request,'iiitdsite/magazine-team.html',{'membersEditor':membersEditor,'membersCS':membersCS,'membersDesign':membersDesign,'membersMC':membersMC})

def financeCommittee(request):
    membersCP = Financial_Committee.objects.filter(tag="Chairperson")
    membersM = Financial_Committee.objects.filter(tag="Member")
    membersMS = Financial_Committee.objects.filter(tag="Non-member")
    return render(request,'iiitdsite/finance_committee.html',{'membersCP':membersCP,'membersM':membersM,'membersMS':membersMS})

def bog(request):
    membersCP = BOG.objects.filter(tag="Chairperson")
    membersM =BOG.objects.filter(tag="Member")
    membersMS = BOG.objects.filter(tag="Non-member")
    return render(request,'iiitdsite/board_of_governers.html',{'membersCP':membersCP,'membersM':membersM,'membersMS':membersMS})

def senate(request):
    membersCP = Senate.objects.filter(tag="Chairperson")
    membersM = Senate.objects.filter(tag="Member")
    membersMS = Senate.objects.filter(tag="Non-member")
    return render(request,'iiitdsite/senate.html',{'membersCP':membersCP,'membersM':membersM,'membersMS':membersMS})


def campus(request):
    return render(request,'iiitdsite/campus.html')


def clubs(request):
    s = Clubs.objects.all()
    return render(request,'iiitdsite/clubs.html', {'s':s})

def admissionProcedure(request):
    return render(request,'iiitdsite/admission_procedure.html')

def fees(request):
    return render(request,'iiitdsite/fees.html')

class AnnouncementsListView(ListView):
     model = Announcements
     template_name = 'iiitdsite/announcements.html'
     ordering = ['-date']
     
class UpdatesListView(ListView):
     model = Updates
     template_name = 'iiitdsite/updates.html'
     ordering = ['-date']

class EventsListView(ListView):
     model = Events
     template_name = 'iiitdsite/events.html'
     ordering = ['-date']

class JobsListView(ListView):
     model = Jobs
     template_name = 'iiitdsite/jobs.html'
     ordering = ['-date']

class TendersListView(ListView):
     model = Tenders
     template_name = 'iiitdsite/tenders.html'
     ordering = ['-publishedDate']

class FacultyDetailPage(DetailView):
    model = Faculty
    template_name = 'iiitdsite/facultyinfo.html'
    

class GalleryCategories(ListView):
    model = Gallery_categories
    template_name = 'iiitdsite/gallery.html'

def gallery(request, cat_id):
    images = Images.objects.all().filter(category_id=cat_id)
    context = {
        "images": images
    }
    return render(request,'iiitdsite/galleryDetail.html',context)
