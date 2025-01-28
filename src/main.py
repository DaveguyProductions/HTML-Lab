import cherrypy
import mako.template
import os.path

PYPATH = os.path.dirname(__file__)

class App:
    @cherrypy.expose
    def index(self):
        t = mako.template.Template(filename=f"{PYPATH}/../html/home.html")
        return t.render(foobar = "NAME")
    
    @cherrypy.expose
    def signup(self):
        t = mako.template.Template(filename=f"{PYPATH}/../html/signup.html")
        return t.render()

    @cherrypy.expose
    def posts(self):
        t = mako.template.Template(filename=f"{PYPATH}/../html/posts.html")
        return t.render()

app = App()
cherrypy.quickstart(app, "/",
    {
        "/media" : {
            "tools.staticdir.on" : True,
            "tools.staticdir.dir" : f"{os.path.dirname(__file__)}/../media"
        }
    }
)