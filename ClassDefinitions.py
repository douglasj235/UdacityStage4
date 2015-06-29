__author__ = 'Jerry'

import webapp2
from google.appengine.ext import ndb
class Concept(ndb.model):
    name = ndb.StringProperty
    description=ndb.StringProperty


class Topic:
    # __init__ runs any time a new instance of Topic is created
    def __init__(self, name='',
                 description=''):  # Parameters assigned a value are optional. So by assigning name={} in the declaration, it means
        # name will be empty if the user doesn't specify one.
        self.name = name
        self.description = description
        self.subtopics = []  # Initialize an empty array to store subtopics. (Spoiler: the subtopics will themselves use the Topics class!)

        # defines a method to add subtopics to a topic

    def add_subtopic(self, subtopic_name,
                     subtopic_description):  # note that subtopic_name and subtopic_description are NOT OPTIONAL
        self.subtopics.append(
            Topic(subtopic_name, subtopic_description))  # our subtopics are simply a list of Topic objects

    # lists all subtopics
    def list_subtopics(self):
        for listed in self.subtopics:
            print listed.name
            print listed.description