import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


from mongoengine import *
connect('gter_bbs')

class personal_status(Document):
    applied_school=StringField()
    degree=StringField()
    subject=StringField()
    applied_result=StringField()
    start_time=StringField()
    start_term=StringField()
    anonnced_time=StringField()


    toefl=StringField()
    gre=StringField()
    undergraduate_school=StringField()
    undergraduate_subject=StringField()
    gpa=StringField()


    url=StringField()
