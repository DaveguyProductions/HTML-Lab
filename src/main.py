import cherrypy
import mako.template
import os.path
import dictionaries
import random 

PYPATH = os.path.dirname(__file__)

class App:
    @cherrypy.expose
    def index(self):
        n = random.choice(dictionaries.names)
        t = mako.template.Template(filename=f"{PYPATH}/../html/home.html")
        return t.render(NAME = n)
    
    @cherrypy.expose
    def signup(self):
        t = mako.template.Template(filename=f"{PYPATH}/../html/signup.html")
        return t.render()

    @cherrypy.expose
    def posts(self):
        i = random.choice(dictionaries.images)
        v = random.randint(0,100000)
        d = random.randint(0,365)
        t = mako.template.Template(filename=f"{PYPATH}/../html/posts.html")
        return t.render(IMAGES = i, VIEWS = v, DAYS = d)

app = App()
cherrypy.quickstart(app, "/",
    {
        "/media" : {
            "tools.staticdir.on" : True,
            "tools.staticdir.dir" : f"{os.path.dirname(__file__)}/../media"
        }
    }
)