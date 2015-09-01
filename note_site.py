import os
from notes import note

import cgi
import urlparse
import urllib

from google.appengine.ext import ndb

import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
            autoescape = True)

def comment_key(comment_name):
    return ndb.Key('comments', comment_name)

class Comment(ndb.Model):
    author = ndb.StringProperty(indexed=False)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        self.render("index.html")

class Lesson(Handler):
    def get(self):

        concepts = self.request.get("lesson")

        if concepts == '':
            url = self.request.url
            parsed_url = urlparse.urlparse(url)
            concepts = parsed_url.params

        comments_query = Comment.query(ancestor=comment_key("lesson" + concepts)).order(Comment.date)
        try:
            concepts = int(concepts)
        except ValueError:
            self.redirect("/")

        comments = comments_query.fetch()

        if concepts < len(note) and concepts >= 0:
            self.render("lesson.html", concepts=note[concepts], lessonnum=concepts, comments=comments)
        else:
            self.redirect("/")

class PostComment(Handler):
    def post(self):
        comment_section = self.request.get("number")
        lessonnum = str(comment_section)

        comment_section = "lesson" + lessonnum
        comment = Comment(parent=comment_key(comment_section))

        comment.content = self.request.get('content')
        comment.author = self.request.get('author')

        if comment.author.isspace() == True or len(comment.author) == 0:
            comment.author = "Anonymous Poster"

        if comment.content.isspace() == False and len(comment.content) > 0:
            comment.put()

        self.redirect('/lesson?lesson=' + lessonnum)

        

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/lesson', Lesson),
                               ('/lesson/post', PostComment),
                               ],
                                debug=True)