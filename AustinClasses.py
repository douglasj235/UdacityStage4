__author__ = 'Jerry'

from google.appengine.ext import ndb
import cgi
import string

#variables representing things that don't change are denoted in all caps

class Concept(ndb.Model):
    name = ndb.StringProperty()
    description = ndb.StringProperty()

class ConceptPage(ndb.Model):
    title = ndb.StringProperty()
    #using repeated=True makes it behave like a list....BUT
    #BEWARE -- you can only have one non-LocalStructuredProperty set to repeated=True!
    comments=ndb.StringProperty(repeated=True)
    #use LcalStructuredProperty for now -- will explain later
    concepts = ndb.LocalStructuredProperty(Concept, repeated=True)

    error_message=''

    #create a method to add a concept
    def add_concept(self, arg_title='', arg_description=''):
        new_concept = Concept(name=arg_title, description=arg_description)
        self.concepts.append(new_concept)



    def read_notes_file(self):
        self.title='Intro to Programming - Stage 4'
        new_name=''
        new_description=''
        notes_file=open('course_notes','r')
        for line in notes_file:
            line=line.strip('')
            line=line.replace("\n","")
            if line[0:6].lower()=='topic ':
                if new_description != '':
                    self.add_concept(new_name,new_description)
                    new_description=''
                new_name=line[6:]

            else:
                if line != '':
                    if new_description == '':
                        new_description=new_description+line[:]
        self.add_concept(new_name,new_description)
        self.put()




    #create a method to add a comment
    def add_comment(self,new_comment):
        self.comments.append(new_comment)
        self.put()