from __future__ import absolute_import

import unittest
from urllib.parse import urlparse

import serve


class PageCase(unittest.TestCase):
    def setUp(self):
        serve.app.config['TESTING'] = True
        self.app = serve.app.test_client()

    def test_index_load(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Vision Statement', response.get_data())

    def test_home_load(self):
        response = self.app.get('/home')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(urlparse(response.location).path, '/')

    def test_about_us_load(self):
        response = self.app.get('/AboutUs')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Us', response.get_data())

    def test_capabilities_load(self):
        response = self.app.get('/Capabilities')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Capabilities', response.get_data())

    def test_careers_load(self):
        response = self.app.get('/Careers')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Careers', response.get_data())

    def test_case_studies_load(self):
        response = self.app.get('/CaseStudies')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Case Studies', response.get_data())

    def test_contact_load(self):
        response = self.app.get('/Contact')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Contact', response.get_data())

    def test_experience_load(self):
        response = self.app.get('/Experience')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Experience', response.get_data())

    def test_references_load(self):
        response = self.app.get('/References')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'References', response.get_data())

    def test_technology_load(self):
        response = self.app.get('/Technology')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Technology', response.get_data())


if __name__ == '__main__':
    unittest.main()
