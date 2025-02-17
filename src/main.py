import cherrypy
import mako.template
import os.path
import dictionaries
import random 
import mako.lookup

PYPATH = os.path.dirname(__file__)

lookup = mako.lookup.TemplateLookup(
    directories=[
        os.path.dirname(__file__),
        f"{os.path.dirname(__file__)}/../html"
    ]
)


class App:
    @cherrypy.expose
    def index(self):
        n = random.choice(dictionaries.names)
        t = lookup.get_template("home.html")
        return t.render(NAME = n)
    
    @cherrypy.expose
    def signup(self):
        t = lookup.get_template("signup.html")
        return t.render()

    @cherrypy.expose
    def posts(self):
        i = random.choice(dictionaries.images)
        v = random.randint(0,100000)
        d = random.randint(0,365)
        t = lookup.get_template("posts.html")
        return t.render(IMAGES = i, VIEWS = v, DAYS = d)

app = App()
cherrypy.quickstart(app, "/",
    {
        "/html" : {
            "tools.staticdir.on" : True,
            "tools.staticdir.dir" : f"{os.path.dirname(__file__)}/../html"
        }
    }
)
  

app = App()
cherrypy.quickstart(app, "/",
    {
        "/media" : {
            "tools.staticdir.on" : True,
            "tools.staticdir.dir" : f"{os.path.dirname(__file__)}/../media"
        }
    }
)
#code



