# encoding: utf-8
import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__name__), 'Templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape = True)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)
	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)
	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class index(Handler):
	def get(self):
		self.render("index.html")
		


application = webapp2.WSGIApplication([
    ('/',index)
], debug=True)