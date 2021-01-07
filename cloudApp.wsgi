#flaskapp.wsgi
import sys 
sys.path.insert(0, '/var/www/html/cloudApp')
  
from cloudApp import app as application
