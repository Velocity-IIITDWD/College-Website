from django.contrib import admin
from django.contrib.auth.models import Group
from .models import AcademicsDSAI, Announcements, Faculty, Image_category,Image, Magazine_Issues, Magazine_Team, NewsPage, NewsLetterEmail, Events, EventsImages, AboutUsTestimonial, Tenders, Updates
from .models import OurFamilyLink, About, AcademicsCSE, AcademicsECE, Academics, ResearchPoints, ResearchStudents
from .models import CurriculumLink, AcademicCalLink, HomePageUpcomingEvents,Senate,BOG,Financial_Committee, Administration, Staff
from .models import ugcselinks, phdlinks, Scholarship, Alert, Jobs, HomePageGallery, Placements, CampusPageDetails, Clubs

admin.site.site_header = 'Admin Panel'


admin.site.register(NewsPage)
admin.site.register(Faculty)
admin.site.register(NewsLetterEmail)
admin.site.register(Events)
admin.site.register(EventsImages)
admin.site.register(About)
admin.site.register(AboutUsTestimonial)
admin.site.register(OurFamilyLink)
admin.site.register(AcademicsCSE)
admin.site.register(AcademicsECE)
admin.site.register(AcademicsDSAI)
admin.site.register(Academics)
admin.site.register(ResearchPoints)
admin.site.register(ResearchStudents)
admin.site.register(CurriculumLink)
admin.site.register(AcademicCalLink)
admin.site.register(HomePageUpcomingEvents)
admin.site.register(Senate)
admin.site.register(Financial_Committee)
admin.site.register(BOG)
admin.site.register(Staff)
admin.site.register(Administration)
admin.site.register(ugcselinks)
admin.site.register(phdlinks)
admin.site.register(Scholarship)
admin.site.register(Alert)
admin.site.register(Jobs)
admin.site.register(Placements)
admin.site.register(CampusPageDetails)
admin.site.register(Announcements)
admin.site.register(Updates)
admin.site.register(Tenders)
admin.site.register(Magazine_Issues)
admin.site.register(Magazine_Team)
admin.site.register(Clubs)
admin.site.register(Image_category)
admin.site.register(Image)

list_display = ['image_tag']