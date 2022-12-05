from django.test import TestCase
from django.urls import reverse, resolve
from nctts.homepage.views import login_user, login_success, login_failed
from django import setup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nctts.settings")
setup()

#Checking to test if homepage url is called and runs with no errors.
class HomepageURLTest(TestCase):

    def test_login_user(self):
        url = reverse('login_user')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_user)
    
    def test_login_success(self):
        url = reverse('login_success')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_success)
        
    def test_login_failed(self):
        url = reverse('login_failed')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_failed)