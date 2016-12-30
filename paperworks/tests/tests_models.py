import os

from django.test import TestCase

from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User

from tests.models import Sender, Recipient, Tag, Papermail

class SenderTestCase(TestCase):
    
    def create_sender(self, name = 'Friendly Sender'):
        
        return Sender.objects.create(name = name)
        
    def test_create_sender(self):
        
        m = self.create_sender()
        self.assertTrue(isinstance(m, Sender))
        self.assertEqual(m.__str__(), m.name)

class RecipientTestCase(TestCase):
    
    def create_recipient(self, name = 'Friendly Recipient'):
        
        return Recipient.objects.create(name = name)
        
    def test_create_recipient(self):
        
        m = self.create_recipient()
        self.assertTrue(isinstance(m, Recipient))
        self.assertEqual(m.__str__(), m.name)
        
class TagTestCase(TestCase):
    
    def create_tag(self, name = 'amazing tag'):
        
        return Tag.objects.create(name = name)
        
    def test_create_tag(self):
        
        m = self.create_tag()
        self.assertTrue(isinstance(m, Tag))
        self.assertEqual(m.__str__(), m.name)
        
class PapermailTestCase(TestCase):
    
    def create_papermail(self, name_file = 'my papermail',date_paper = '1970-01-01' ):
        
        paper_file = SimpleUploadedFile(name='test_image.jpg', content=open('paperworks/tests/test_image.jpg', 'rb').read(), content_type='image/jpeg')
        s = Sender.objects.create(name = 'Friendly Sender')
        r = Recipient.objects.create(name = 'Friendly Recipient')
        property_of = User.objects.create(username = 'Paul')
        
        return Papermail.objects.create(name_file = name_file, paper_file = paper_file, sender = s,recipient = r, date_paper = date_paper, property_of = property_of)
        
    def test_create_papermail(self):
        
        m = self.create_papermail()
        self.assertTrue(isinstance(m, Papermail))
        self.assertEqual(m.__str__(), m.name_file)
# remove the file create by the test
        os.remove(m.paper_file.path)