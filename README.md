# Customer Management
This is a basic CRUD app in front end and it's calling api for data.

#Tech used:
| Title | Description | link |
| ----- | ----- | ----- |
| Django | Provides Api for the front end | https://www.django-rest-framework.org/ |
| Vue js | High level Javascript framework to make our job easy | https://vuejs.org/ |
| Tailwindcss | It provides UI framework | https://tailwindcss.com/ |

# Instructions to run a project
For Front end:
- use `index.html` file

For Bach end:
- use `customermanagementapi` folder that's where Django rest framework app placed.

Make sure running the below codes before executing front end file

```
cd customermanagementapi
python -m venv cmapi
pip install -r requirements.txt
python manage.py runserver
```
That's it after executing the above code we are good to run `index.html` file we can do the crud operations for customers management.
