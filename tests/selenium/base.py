#!/usr/bin/python

# To run these tests you must copy one of the example files to "creds.py" in
# this directory, and edit it for your environment. There are 2 example files
# in this directory:
#
# remote_creds.example.py:  Configure the Selenium tests to run with BrowserStack
# local_creds.example.py:   Configure the Selenium tests to run locally

from time import sleep
from creds import SITE_URL, USER, PASS, get_driver
from selenium.common import exceptions

SLEEP_INT = 1
MODULES = 'core,contacts,local_contacts,ldap_contacts,gmail_contacts,feeds,'
MODULES += 'pop3,imap,smtp,site,account,idle_timer,calendar,themes,nux,'
MODULES += 'developer,wordpress,github,history,saved_searches,inline_message,'
MODULES += 'profiles,imap_folders,password_restrictions,nasa,keyboard_shortcuts,'
MODULES += '2fa,recover_settings'

class WebTest:

    driver = None

    def __init__(self, cap=None):
        self.driver = get_driver(cap)
        self.load()

    def load(self):
        self.go(SITE_URL)

    def mod_active(self, name):
        if name in ','.split(MODULES):
            return True
        print " - module not enabled: %s" % name
        return False

    def go(self, url):
        self.driver.get(url)

    def rest(self):
        sleep(SLEEP_INT)

    def login(self, user, password):
        user_el = self.by_name('username')
        pass_el = self.by_name('password')
        user_el.send_keys(user)
        pass_el.send_keys(password)
        self.by_id('login').click()

    def change_val(self, el, val):
        self.driver.execute_script('''
            var e=arguments[0]; var v=arguments[1]; e.value=v;''',
            el, val)

    def logout(self):
        self.driver.find_element_by_class_name('logout_link').click()
        try:
            logout = self.by_id('logout_without_saving')
            if logout:
                logout.click()
        except:
            pass

    def end(self):
        self.driver.quit()

    def by_id(self, el_id):
        try:
            return self.driver.find_element_by_id(el_id)
        except exceptions.NoSuchElementException:
            return None

    def by_name(self, name):
        try:
            return self.driver.find_element_by_name(name)
        except exceptions.NoSuchElementException:
            return None

    def by_css(self, selector):
        try:
            return self.driver.find_element_by_css_selector(selector)
        except exceptions.NoSuchElementException:
            return None

    def by_class(self, class_name):
        try:
            return self.driver.find_element_by_class_name(class_name)
        except exceptions.NoSuchElementException:
            return None
