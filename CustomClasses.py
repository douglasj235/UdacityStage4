__author__ = 'Jerry'

from google.appengine.ext import ndb
import csv

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



    def read_notes_file(self,filename='course_notes.csv'):
        notes_file=open(filename,'r')
        file_reader=csv.reader(notes_file,delimiter='|')
        for new_line in file_reader:
            new_name=new_line[0]
            new_description=new_line[1]
            self.add_concept(new_name,new_description)
        self.put()
        notes_file.close()





    #create a method to add a comment
    def add_comment(self,new_comment):
        self.comments.append(new_comment)
        self.put()