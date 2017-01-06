from __future__ import absolute_import

import unittest
from urllib.parse import urlparse

import serve


class PageCase(unittest.TestCase):
    def setUp(self):
        serve.app.config['TESTING'] = True
        self.app = serve.app.test_client()

    def test_index_load(self):
        self.page_test('/', b'Vision Statement')

    def test_home_load(self):
        response = self.app.get('/home')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(urlparse(response.location).path, '/')

    def test_about_us_load(self):
        self.page_test('/AboutUs', b'About Us')

    def test_capabilities_load(self):
        self.page_test('/Capabilities', b'Capabilities')

    def test_careers_load(self):
        self.page_test('/Careers', b'Careers')

    def test_case_studies_load(self):
        self.page_test('/CaseStudies', b'Case Studies')

    def test_contact_load(self):
        self.page_test('/Contact', b'Contact')

    def test_experience_load(self):
        self.page_test('/Experience', b'Experience')

    def test_references_load(self):
        self.page_test('/References', b'References')

    def test_technology_load(self):
        self.page_test('/Technology', b'Technology')

    def test_robots_load(self):
        self.page_test('/robots.txt', b'')

    def test_sitemap_load(self):
        self.page_test('/sitemap.xml', b'xml')

    def page_test(self, path, string):
        response = self.app.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertIn(string, response.get_data())
