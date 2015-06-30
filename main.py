import jinja2
import webapp2
import os
from CustomClasses import *

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


class MainHandler(webapp2.RequestHandler):

    concepts_page = ConceptPage.query().get()


    if not concepts_page:
        concepts_page = ConceptPage()
        concepts_page.title = 'Intro to Programming - Stage 4'
        concepts_page.read_notes_file()

    def get(self):
        template_values = {
            'concepts_page': self.concepts_page,
            'error_message': self.concepts_page.error_message
        }

        template = jinja_env.get_template('concepts_page.html')
        self.response.write(template.render(template_values))
        self.concepts_page.error_message=''

    def post(self):
        new_comment= self.request.get('new_comment')

        if new_comment == '':
            self.concepts_page.error_message='Please enter a non-empty comment'
            self.redirect('/')
        else:
            self.concepts_page.add_comment(new_comment)
            self.concepts_page.put()
            self.redirect('/')


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
