import site
import sys

site.addsitedir("/root/watertruck-env/lib/python2.7/site-packages")
activate = "/root/watertruck-env/bin/activate_this.py"
execfile(activate, dict(__file__=activate_this))

from watertruck import service as application
