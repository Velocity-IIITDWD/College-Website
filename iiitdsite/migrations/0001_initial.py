# Generated by Django 3.2.6 on 2022-11-11 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_image_link', models.ImageField(blank=True, null=True, upload_to='Director/')),
                ('chairperson_image_link', models.ImageField(blank=True, null=True, upload_to='Chairperson/')),
            ],
        ),
        migrations.CreateModel(
            name='AboutUsTestimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='About/')),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('name_hindi', models.CharField(max_length=50)),
                ('position_hindi', models.CharField(max_length=50)),
                ('description_hindi', models.CharField(max_length=300)),
                ('name_kannada', models.CharField(max_length=50)),
                ('position_kannada', models.CharField(max_length=50)),
                ('description_kannada', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='AcademicCalLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acad_link', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Academics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cse_image_link', models.CharField(max_length=200)),
                ('ece_image_link', models.CharField(max_length=200)),
                ('academic_calendar_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AcademicsCSE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=3000)),
                ('description_hindi', models.CharField(max_length=3000)),
                ('description_kannada', models.CharField(max_length=3000)),
                ('academic_calendar_link', models.CharField(max_length=200)),
                ('curriculum_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AcademicsDSAI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=3000)),
                ('description_hindi', models.CharField(max_length=3000)),
                ('description_kannada', models.CharField(max_length=3000)),
                ('academic_calendar_link', models.CharField(max_length=200)),
                ('curriculum_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AcademicsECE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=3000)),
                ('description_hindi', models.CharField(max_length=3000)),
                ('description_kannada', models.CharField(max_length=3000)),
                ('academic_calendar_link', models.CharField(max_length=200)),
                ('curriculum_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Administration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_hindi', models.CharField(max_length=100)),
                ('name_kannada', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=300)),
                ('position_hindi', models.CharField(max_length=300)),
                ('position_kannada', models.CharField(max_length=300)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Administration/')),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.CharField(max_length=200)),
                ('news_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('subtitle', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BOG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('role', models.CharField(max_length=200, null=True)),
                ('tag', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='BOG/')),
            ],
        ),
        migrations.CreateModel(
            name='CampusPageDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_hindi', models.CharField(max_length=100)),
                ('title_kannada', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=3000)),
                ('description_hindi', models.CharField(max_length=3000)),
                ('description_kannada', models.CharField(max_length=3000)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='CampusGallery/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='CampusGallery/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='CampusGallery/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='CampusGallery/')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='CampusGallery/')),
                ('image6', models.ImageField(blank=True, null=True, upload_to='CampusGallery/')),
            ],
        ),
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Logo', models.ImageField(blank=True, null=True, upload_to='Clubs/')),
                ('NameofClub', models.CharField(max_length=200)),
                ('Website', models.CharField(blank=True, max_length=200)),
                ('Instalink', models.CharField(blank=True, max_length=200)),
                ('LinkedIn', models.CharField(blank=True, max_length=200)),
                ('Facebook', models.CharField(blank=True, max_length=200)),
                ('Mail', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CurriculumLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cse_link', models.CharField(blank=True, max_length=200)),
                ('ece_link', models.CharField(blank=True, max_length=200)),
                ('dsai_link', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='EventsCover/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('designation', models.CharField(max_length=200, null=True)),
                ('department', models.CharField(max_length=200, null=True)),
                ('mail', models.EmailField(max_length=254, null=True)),
                ('interest', models.CharField(max_length=500, null=True)),
                ('profile', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Faculty/')),
            ],
        ),
        migrations.CreateModel(
            name='Financial_Committee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('role', models.CharField(max_length=200, null=True)),
                ('tag', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='FinanceCommittee/')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Gallery/')),
                ('shape', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Gallery',
            },
        ),
        migrations.CreateModel(
            name='Gallery_categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=500)),
                ('event_date', models.DateTimeField()),
                ('cover', models.ImageField(upload_to='Gallery/')),
            ],
        ),
        migrations.CreateModel(
            name='HomePageGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='HomePageGallery/')),
            ],
        ),
        migrations.CreateModel(
            name='HomePageUpcomingEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=1000)),
                ('description_hindi', models.CharField(max_length=1000)),
                ('description_kannada', models.CharField(max_length=1000)),
                ('location', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='UpcomingEventsCover/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200, null=True)),
                ('date', models.DateField()),
                ('form', models.CharField(blank=True, max_length=200, null=True)),
                ('instructions', models.FileField(blank=True, null=True, upload_to='Jobs/')),
            ],
        ),
        migrations.CreateModel(
            name='Magazine_Issues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Magazine/Issues/')),
                ('file', models.FileField(blank=True, null=True, upload_to='Magazine/Issues/')),
                ('description', models.TextField(blank=True, null=True)),
                ('publishedDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Magazine_Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('role', models.CharField(max_length=200, null=True)),
                ('tag', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Magazine/Team/')),
            ],
        ),
        migrations.CreateModel(
            name='NewsLetterEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NewsPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='News/%Y/%m/%d')),
                ('headline', models.CharField(max_length=300)),
                ('headline_hindi', models.CharField(max_length=300)),
                ('headline_kannada', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=3000)),
                ('description_hindi', models.CharField(max_length=3000)),
                ('description_kannada', models.CharField(max_length=3000)),
                ('news_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OurFamilyLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('name_hindi', models.CharField(max_length=50)),
                ('name_kannada', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=200)),
                ('link_hindi', models.CharField(max_length=200)),
                ('link_kannada', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='phdlinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(null=True)),
                ('form', models.CharField(blank=True, max_length=200, null=True)),
                ('instructions', models.FileField(blank=True, null=True, upload_to='PhdAdmission/')),
            ],
        ),
        migrations.CreateModel(
            name='Placements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='PlacementCompanyLogo/')),
                ('company_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.CharField(max_length=300)),
                ('point_hindi', models.CharField(max_length=300)),
                ('point_kannada', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ResearchStudents/')),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_loan_application', models.CharField(max_length=200)),
                ('checklist', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Senate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('role', models.CharField(max_length=200, null=True)),
                ('tag', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Senate/')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('role', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Staff/')),
            ],
        ),
        migrations.CreateModel(
            name='Tenders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tender_title', models.CharField(max_length=200, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='Tenders/')),
                ('publishedDate', models.DateField()),
                ('lastDate', models.DateField()),
                ('time', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ugcselinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jossa_link', models.CharField(max_length=200)),
                ('csab_link', models.CharField(max_length=200)),
                ('course_seat_matrix', models.CharField(max_length=200)),
                ('admission_checklist', models.CharField(max_length=200)),
                ('fee_structure', models.CharField(max_length=200)),
                ('sbi_collect', models.CharField(max_length=200)),
                ('instructions_sbi_collect', models.CharField(max_length=200)),
                ('academic_regulations', models.CharField(max_length=200)),
                ('scholarships_bank_loans', models.CharField(max_length=200)),
                ('policy', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Updates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('subtitle', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Images/')),
                ('shape', models.CharField(max_length=200)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='iiitdsite.gallery_categories')),
            ],
        ),
        migrations.CreateModel(
            name='EventsImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Events/%Y/%m/%d')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iiitdsite.events')),
            ],
        ),
    ]
