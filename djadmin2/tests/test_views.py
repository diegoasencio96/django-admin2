from django.test import TestCase
from django.views.generic import View

from ..views import AdminView


class AdminViewTest(TestCase):

    def setUp(self):
        self.admin_view = AdminView(r'^$', View)

    def test_url(self):
        self.assertEquals(self.admin_view.url, r'^$')

    def test_view(self):
        self.assertEquals(self.admin_view.view, View)
