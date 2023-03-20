from email.mime import image


from django.db import models
from django.db.models.fields import EmailField
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.html import mark_safe

class Faculty(models.Model):
    name = models.CharField(max_length=200,null=True)
    designation = models.CharField(max_length=200,null=True)
    department  =models.CharField(max_length=200,null=True)
    mail= models.EmailField(null=True)
    interest = models.CharField(max_length=500,null=True)
    profile =  models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='Faculty/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('facultyinfo',args=[str(self.id)])


        



class NewsLetterEmail(models.Model):
    email_id = models.CharField(max_length=100)

    def __str__(self):
        return self.email_id


class Events(models.Model):
    event_name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='EventsCover/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.event_name[:50]


class EventsImages(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Events/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.image_name


class About(models.Model):
    director_image_link = models.ImageField(upload_to='Director/', blank=True, null=True)
    chairperson_image_link = models.ImageField(upload_to='Chairperson/', blank=True, null=True)


class OurFamilyLink(models.Model):
    name = models.CharField(max_length=50)
    name_hindi = models.CharField(max_length=50)
    name_kannada = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    link_hindi = models.CharField(max_length=200)
    link_kannada = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AboutUsTestimonial(models.Model):
    image = models.ImageField(upload_to='About/', blank=True, null=True)
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    name_hindi = models.CharField(max_length=50)
    position_hindi = models.CharField(max_length=50)
    description_hindi = models.CharField(max_length=300)
    name_kannada = models.CharField(max_length=50)
    position_kannada = models.CharField(max_length=50)
    description_kannada = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class AcademicsCSE(models.Model):
    description = models.CharField(max_length=3000)
    description_hindi = models.CharField(max_length=3000)
    description_kannada = models.CharField(max_length=3000)
    academic_calendar_link = models.CharField(max_length=200)
    curriculum_link = models.CharField(max_length=200)


class AcademicsECE(models.Model):
    description = models.CharField(max_length=3000)
    description_hindi = models.CharField(max_length=3000)
    description_kannada = models.CharField(max_length=3000)
    academic_calendar_link = models.CharField(max_length=200)
    curriculum_link = models.CharField(max_length=200)

class AcademicsDSAI(models.Model):
    description = models.CharField(max_length=3000)
    description_hindi = models.CharField(max_length=3000)
    description_kannada = models.CharField(max_length=3000)
    academic_calendar_link = models.CharField(max_length=200)
    curriculum_link = models.CharField(max_length=200)

class Academics(models.Model):
    cse_image_link = models.CharField(max_length=200)
    ece_image_link = models.CharField(max_length=200)
    academic_calendar_link = models.CharField(max_length=200)


class ResearchPoints(models.Model):
    point = models.CharField(max_length=300)
    point_hindi = models.CharField(max_length=300)
    point_kannada = models.CharField(max_length=300)


class ResearchStudents(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ResearchStudents/', blank=True, null=True)

    def __str__(self):
        return self.name


class CurriculumLink(models.Model):
    cse_link = models.CharField(max_length=200, blank=True)
    ece_link = models.CharField(max_length=200, blank=True)
    dsai_link = models.CharField(max_length=200, blank=True)


class NewsPage(models.Model):
    news_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='News/%Y/%m/%d', blank=True, null=True)
    headline = models.CharField(max_length=300)
    headline_hindi = models.CharField(max_length=300)
    headline_kannada = models.CharField(max_length=300)
    description = models.CharField(max_length=3000)
    description_hindi = models.CharField(max_length=3000)
    description_kannada = models.CharField(max_length=3000)
    news_type = models.CharField(max_length=50)


class CampusPageDetails(models.Model):
    title = models.CharField(max_length=100)
    title_hindi = models.CharField(max_length=100)
    title_kannada = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    description_hindi = models.CharField(max_length=3000)
    description_kannada = models.CharField(max_length=3000)
    image1 = models.ImageField(upload_to='CampusGallery/', blank=True, null=True)
    image2 = models.ImageField(upload_to='CampusGallery/', blank=True, null=True)
    image3 = models.ImageField(upload_to='CampusGallery/', blank=True, null=True)
    image4 = models.ImageField(upload_to='CampusGallery/', blank=True, null=True)
    image5 = models.ImageField(upload_to='CampusGallery/', blank=True, null=True)
    image6 = models.ImageField(upload_to='CampusGallery/', blank=True, null=True)

    def __str__(self):
        return self.title


class HomePageUpcomingEvents(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.CharField(max_length=1000)
    description_hindi = models.CharField(max_length=1000)
    description_kannada = models.CharField(max_length=1000)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='UpcomingEventsCover/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.title


class Placements(models.Model):
    logo = models.ImageField(upload_to='PlacementCompanyLogo/', blank=True, null=True)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class AcademicCalLink(models.Model):
    acad_cal = models.FileField(upload_to='Docs/',blank=True)
    acad_cal_name = models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.acad_cal_name


class Administration(models.Model):
    name = models.CharField(max_length=100)
    name_hindi = models.CharField(max_length=100)
    name_kannada = models.CharField(max_length=100)
    position = models.CharField(max_length=300)
    position_hindi = models.CharField(max_length=300)
    position_kannada = models.CharField(max_length=300)
    image = models.ImageField(upload_to='Administration/', blank=True, null=True)

    def __str__(self):
        return self.name

class ugcselinks(models.Model):
    jossa_link = models.CharField(max_length=200)
    csab_link = models.CharField(max_length=200)
    course_seat_matrix = models.CharField(max_length=200)
    admission_checklist = models.CharField(max_length=200)
    fee_structure = models.CharField(max_length=200)
    sbi_collect = models.CharField(max_length=200)
    instructions_sbi_collect = models.CharField(max_length=200)
    academic_regulations = models.CharField(max_length=200)
    scholarships_bank_loans = models.CharField(max_length=200)
    policy = models.CharField(max_length=200)


class phdlinks(models.Model):
    title = models.CharField(max_length=200,null=True)
    date = models.DateField(null=True)
    form= models.CharField(max_length=200,blank=True, null=True)
    instructions = models.FileField(upload_to='PhdAdmission/', blank=True, null=True)

    def __str__(self): 
         return self.title[:50]


class Scholarship(models.Model):
    education_loan_application = models.CharField(max_length=200)
    checklist = models.CharField(max_length=200)


class Alert(models.Model):
    notice = models.CharField(max_length=200)
    news_name = models.CharField(max_length=200)


class Jobs(models.Model):
    job_title = models.CharField(max_length=200)
    description= models.CharField(max_length=100000, null=True)
    date = models.DateField()
    form= models.CharField(max_length=200,blank=True, null=True)
    instructions = models.FileField(upload_to='Jobs/', blank=True, null=True)

    def __str__(self): 
         return self.job_title[:50]

class HomePageGallery(models.Model):
    image = models.ImageField(upload_to='HomePageGallery/', blank=True, null=True)



class Announcements(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
         return self.title[:50]

class Updates(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
         return self.title[:50]

class Tenders(models.Model):
    tender_title = models.CharField(max_length=200,null=True)
    file = models.FileField(upload_to='Tenders/', blank=True, null=True)
    publishedDate= models.DateField()
    lastDate = models.DateField()
    time = models.TimeField(null=True)

    def __str__(self): 
         return self.tender_title[:50]

class Magazine_Issues(models.Model):
    title = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='Magazine/Issues/', blank=True, null=True)
    file = models.FileField(upload_to='Magazine/Issues/', blank=True, null=True)
    description= models.TextField(blank=True, null=True)
    publishedDate= models.DateField()

    def __str__(self): 
         return self.title[:50]

class Magazine_Team(models.Model):
    name = models.CharField(max_length=200,null=True)
    role = models.CharField(max_length=200,null=True)
    tag = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='Magazine/Team/', blank=True, null=True)

    def __str__(self): 
         return self.name[:50]

class Clubs(models.Model):
    Logo = models.ImageField(upload_to='Clubs/', blank=True, null=True)
    NameofClub = models.CharField(max_length=200)
    Website = models.CharField(max_length=200, blank=True)
    Instalink = models.CharField(max_length=200, blank=True)
    LinkedIn = models.CharField(max_length=200, blank=True)
    Facebook = models.CharField(max_length=200, blank=True)
    Mail = models.CharField(max_length=200, blank=True)
    Description=models.TextField(blank=True,null=True)
    identifier=models.CharField(unique=True, max_length=200,null=True,blank=True)

    def __str__(self): 
         return self.NameofClub[:50]
    
class Club_Members(models.Model):
    Name =models.CharField(max_length=30)
    Photo=models.ImageField(upload_to='Clubs/Members/',blank=True,null=True)
    Post=models.CharField(max_length=20)
    identifier=models.CharField(max_length=200,null=True,blank=True)
    NameOfClub=models.ForeignKey(Clubs,on_delete=models.CASCADE)

    def __str__(self):
        return self.Name[:30]


class Senate(models.Model):
    name = models.CharField(max_length=200,null=True)
    role = models.CharField(max_length=200,null=True)
    tag = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='Senate/', blank=True, null=True)

    def __str__(self): 
         return self.name[:50]

class Financial_Committee(models.Model):
    name = models.CharField(max_length=200,null=True)
    role = models.CharField(max_length=200,null=True)
    tag = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='FinanceCommittee/', blank=True, null=True)

    def __str__(self): 
         return self.name[:50]

class BOG(models.Model):
    name = models.CharField(max_length=200,null=True)
    role = models.CharField(max_length=200,null=True)
    tag = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='BOG/', blank=True, null=True)

    def __str__(self): 
         return self.name[:50]

class Staff(models.Model):
    name = models.CharField(max_length=200,null=True)
    role = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='Staff/', blank=True, null=True)

    def __str__(self): 
         return self.name[:50]


#Configuring the Gallery Page



class Image_category(models.Model):
    event_name = models.CharField(max_length=500)
    event_date = models.DateTimeField()
    cover = models.ImageField(upload_to = 'Gallery/')

    def __str__(self):
        return self.event_name[:50]

    def get_absolute_url(self):
        return reverse('galleryDetail',args=[str(self.id)])

class Image(models.Model):
    category = models.ForeignKey(to=Image_category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='Images/')
    shape = models.CharField(max_length=200)  

    def __str__(self):
        return str(self.category)
    
class Nirf(models.Model):
    title = models.CharField(max_length=1000,null=True)
    report = models.FileField(upload_to='NIRF/Reports',null=True,blank=True)
            
    def __str__(self):
        return str(self.title)



