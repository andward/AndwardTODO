# Andward.TODO
TODO management and reassignment platform which named Andward.

##Installation (Linux)

-Clone project from github.

<code>git clone https://github.com/andward/AndwardTODO.git</code>

-Install reqirment packages (make sure you already has pip).

<code>pip install -r requirements.txt</code>

##Setup your database

-Make sure you has MySQL in your linux.

-Create a database (exp: todo)

<code>Create database todo character set utf8</code>

-Config your database information in settings.py

<code>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # mysql<br />
        'NAME': 'todo',                      # Your database name<br />
        'USER': 'root',                      # root<br />
        'PASSWORD': 'your password',    # your root password<br />
        'HOST': 'localhost',     # Set to empty string for localhost. Not used with sqlite3.<br />
        'PORT': '3306',<br />                
    }
}
<code>

##Go to project folder and sync database

<code>cd AndwardTODO</code>
<code>python manage.py syncdb</code>

## Start local server
<code>python manage.py runserver</code>

Then, run http://127.0.0.1:8000/task/tag/ALL, you will see the UI.




