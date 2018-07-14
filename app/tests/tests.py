from __future__ import absolute_import

import unittest
from urllib.parse import urlparse

from app import serve


class PageCase(unittest.TestCase):
    def setUp(self):
        serve.app.config['TESTING'] = True
        self.app = serve.app.test_client()

    def test_index_load(self):
        self.page_test('/', b'Vision Statement')

    def test_about_us_load(self):
        self.page_test('/about_us', b'About Us')

    def test_capabilities_load(self):
        self.page_test('/capabilities', b'Capabilities')

    def test_careers_load(self):
        self.page_test('/careers', b'Careers')

    def test_case_studies_load(self):
        self.page_test('/case_studies', b'Case Studies')

    def test_contact_load(self):
        self.page_test('/contact', b'Contact')

    def test_experience_load(self):
        self.page_test('/experience', b'Experience')

    def test_references_load(self):
        self.page_test('/references', b'References')

    def test_technology_load(self):
        self.page_test('/technology', b'Technology')

    def test_robots_load(self):
        self.page_test('/robots.txt', b'')

    def test_sitemap_load(self):
        self.page_test('/sitemap.xml', b'xml')

    def test_not_found(self):
        response = self.app.get('/asdf')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Not Found', response.get_data())

    def page_test(self, path, string):
        response = self.app.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertIn(string, response.get_data())

    def test_about_us_redirect(self):
        self.redirect_test('/AboutUs', '/about_us')

    def test_capabilities_redirect(self):
        self.redirect_test('/Capabilities', '/capabilities')

    def test_careers_redirect(self):
        self.redirect_test('/Careers', '/careers')

    def test_case_studies_redirect(self):
        self.redirect_test('/CaseStudies', '/case_studies')

    def test_contact_redirect(self):
        self.redirect_test('/Contact', '/contact')

    def test_experience_redirect(self):
        self.redirect_test('/Experience', '/experience')

    def test_references_redirect(self):
        self.redirect_test('/References', '/references')

    def test_technology_redirect(self):
        self.redirect_test('/Technology', '/technology')

    def test_home_load(self):
        self.redirect_test('/home', '/')

    def redirect_test(self, path, new_path):
        response = self.app.get(path)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(urlparse(response.location).path, new_path)

    def test_404(self):
        response = self.app.get('/asdf')
        self.assertEqual(response.status_code, 404)
