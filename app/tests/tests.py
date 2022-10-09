import unittest
from urllib.parse import urlparse

from varsnap import test

from app import serve


class PageCase(unittest.TestCase):
    def setUp(self) -> None:
        serve.app.config['TESTING'] = True
        self.app = serve.app.test_client()

    def test_index_load(self) -> None:
        self.page_test('/', b'Vision Statement')

    def test_about_us_load(self) -> None:
        self.page_test('/about_us', b'About Us')

    def test_capabilities_load(self) -> None:
        self.page_test('/capabilities', b'Capabilities')

    def test_careers_load(self) -> None:
        self.page_test('/careers', b'Careers')

    def test_case_studies_load(self) -> None:
        self.page_test('/case_studies', b'Case Studies')

    def test_contact_load(self) -> None:
        self.page_test('/contact', b'Contact')

    def test_experience_load(self) -> None:
        self.page_test('/experience', b'Experience')

    def test_references_load(self) -> None:
        self.page_test('/references', b'References')

    def test_technology_load(self) -> None:
        self.page_test('/technology', b'Technology')

    def test_robots_load(self) -> None:
        self.page_test('/robots.txt', b'')

    def test_security_load(self) -> None:
        self.page_test('/.well-known/security.txt', b'Contact')

    def test_humans_load(self) -> None:
        self.page_test('/humans.txt', b'albertyw')

    def test_health_load(self) -> None:
        self.page_test('/health', b'ok')

    def test_sitemap_load(self) -> None:
        self.page_test('/sitemap.xml', b'xml')

    def test_not_found(self) -> None:
        response = self.app.get('/asdf')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Not Found', response.get_data())

    def page_test(self, path: str, string: bytes) -> None:
        response = self.app.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertIn(string, response.get_data())
        response.close()

    def test_about_us_redirect(self) -> None:
        self.redirect_test('/AboutUs', '/about_us')

    def test_capabilities_redirect(self) -> None:
        self.redirect_test('/Capabilities', '/capabilities')

    def test_careers_redirect(self) -> None:
        self.redirect_test('/Careers', '/careers')

    def test_case_studies_redirect(self) -> None:
        self.redirect_test('/CaseStudies', '/case_studies')

    def test_contact_redirect(self) -> None:
        self.redirect_test('/Contact', '/contact')

    def test_experience_redirect(self) -> None:
        self.redirect_test('/Experience', '/experience')

    def test_references_redirect(self) -> None:
        self.redirect_test('/References', '/references')

    def test_technology_redirect(self) -> None:
        self.redirect_test('/Technology', '/technology')

    def test_home_load(self) -> None:
        self.redirect_test('/home', '/')

    def redirect_test(self, path: str, new_path: str) -> None:
        response = self.app.get(path)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(urlparse(response.location).path, new_path)

    def test_404(self) -> None:
        response = self.app.get('/asdf')
        self.assertEqual(response.status_code, 404)


class TestIntegration(unittest.TestCase):
    def test_varsnap(self) -> None:
        serve.app.config['SERVER_NAME'] = 'www.pharmadataassociates.com'
        with serve.app.test_request_context(
            environ_overrides={'wsgi.url_scheme': 'https'}
        ):
            matches, logs = test()
        if matches is None:
            raise unittest.case.SkipTest('No Snaps found')  # pragma: no cover
        self.assertTrue(matches, logs)
