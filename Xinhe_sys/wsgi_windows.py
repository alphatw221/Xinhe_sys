
# activate_this = 'D:/programdata/anaconda3/envs/conda_env/Scripts/'
# # execfile(activate_this, dict(__file__=activate_this))
# exec(open(activate_this).read(),dict(__file__=activate_this))

import os
import sys
import site
from django.core.wsgi import get_wsgi_application
# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('D:/programdata/anaconda3/envs/conda_env/lib/site-packages')




# Add the app's directory to the PYTHONPATH
sys.path.append('C:/Users/tnt/Desktop/Xinhe_sys')
sys.path.append('C:/Users/tnt/Desktop/Xinhe_sys/Xinhe_sys')
sys.path.append('C:/Users/tnt/Desktop/Xinhe_sys/templates')
sys.path.append('C:/Users/tnt/Desktop/Xinhe_sys/Xinhe_sys')
sys.path.append('C:/Users/tnt/Desktop/Xinhe_sys/static')

os.environ['DJANGO_SETTINGS_MODULE'] = 'Xinhe_sys.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Xinhe_sys.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()