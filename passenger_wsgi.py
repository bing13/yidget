import sys, os

## this points to the VirtualEnv I installed on 2014-06-01
## to provide flask.  See http://wiki.dreamhost.com/Flask
INTERP = os.path.join(os.environ['HOME'], 'f.bernardhecker.com', 'flask_vx', 'bin', 'python')

if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

## the default path has a ton of junk in it, including from Django
## ideally, will rationalize that.  But for now, this static path works... until
## something changes, and then it will be confusing again.
    
sys.path = ['/home/bhadmin13/f.bernardhecker.com/flask_vx/local/lib/python2.7/site-packages/distribute-0.6.24-py2.7.egg', '/home/bhadmin13/f.bernardhecker.com/flask_vx/local/lib/python2.7/site-packages/pip-1.1-py2.7.egg', '/home/bhadmin13/f.bernardhecker.com/flask_vx/lib/python2.7/site-packages/distribute-0.6.24-py2.7.egg', '/home/bhadmin13/f.bernardhecker.com/flask_vx/lib/python2.7/site-packages/pip-1.1-py2.7.egg', '/home/bhadmin13/python_pkgs', '/home/bhadmin13/python_pkgs/lib/python2.5/site-packages', '/home/bhadmin13/f.bernardhecker.com/flask_vx/lib/python2.7', '/home/bhadmin13/f.bernardhecker.com/flask_vx/lib/python2.7/plat-linux2', '/home/bhadmin13/f.bernardhecker.com/flask_vx/lib/python2.7/lib-tk', '/home/bhadmin13/f.bernardhecker.com/flask_vx/lib/python2.7/lib-old', '/home/bhadmin13/f.bernardhecker.com/flask_vx/lib/python2.7/lib-dynload', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-linux2', '/usr/lib/python2.7/lib-tk', '/home/bhadmin13/f.bernardhecker.com/flask_vx/local/lib/python2.7/site-packages', '/home/bhadmin13/f.bernardhecker.com/flask_vx/lib/python2.7/site-packages']
    
sys.path.append(os.getcwd())
from yidget.yidget_main import flaskRoute as application

# Uncomment next two lines to enable debugging
from werkzeug.debug import DebuggedApplication
application = DebuggedApplication(application, evalex=True)
