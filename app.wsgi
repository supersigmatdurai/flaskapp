import sys
sys.path.insert(0,'/var/www/basic-flask-app/flaskapp')


activate_this = '/home/akash1/.local/share/virtualenvs/flaskapp-ejC1LiSe/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(),dict(__file__ = activate_this))


from app import app as application
