
```sh
pipenv shell
```

When you fork the repo and open the code for the first time:
```sh
pip install -r requirements.txt
```

If (css or js or images have been changed):

```sh
python manage.py collectstatic --settings=collegesite.settings_local
```

If (backend or db/models.py has been changed):

```sh	
python manage.py makemigrations --settings=collegesite.settings_local
```

```sh
python manage.py migrate --settings=collegesite.settings_local
```


For giving yourself admin access to your local server:
```sh	
python manage.py createsuperuser --settings=collegesite.settings_local
```

For running the local server:
```sh
python manage.py runserver --settings=collegesite.settings_local
```

You won't be able to see any pictures or data once you run the code. This is because no data has been added to your local db in admin panel.
Wherever you make a change, go to your local server url/admin (127.0.0.1/admin), login into the admin panel, and if suppose you have changed about,
then go to the about model in the admin panel and add the data.

Initially if the site doesn't run using the run server command and shows an error, go the admin panel and add dummy links for acadcallinks
and curriculumlinks model.

Backend team please not if you make a new model in models.py, you have to register it in admin.py 

Any change that gets approved on the development branch will be visible on 

https://iiit-dwd-website-development.herokuapp.com/

For the change that you make, you also have to add the data for that change in the admin panel in this url.

The credentials for the admin panel of this url are:
```sh
username: velocity
password: velocity
```
