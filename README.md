# Andward.TODO
TODO web tool which named Andward

##Installation (Linux)

-Clone project from github.
<code>git clone https://github.com/andward/AndwardTODO.git</code>

-Install reqirment packages (make sure you already has pip).
<code>pip install -r requirements.txt</code>

##Setup your database

-Make sure you has MySQL in your linux.
-Create a database (exp: todo)
<code>create database todo character set utf8</code>
-Config your database information in settings.py
{% highlight ruby %}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # mysql, 'sqlite3' or 'oracle'.
        'NAME': 'todo',                      # Your database name
        'USER': 'root',                      # root
        'PASSWORD': 'your password',    # your root password
        'HOST': 'localhost',     # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                 
    }
}
{% endhighlight %}
- Go to project folder and sync database
<code>cd AndwardTODO</code>
<code>python manage.py syncdb</code>

## Start local server
<code>python manage.py runserver</code>

Then, run http://127.0.0.1:8000/task/tag/ALL, you will see the UI.




