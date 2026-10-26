from django.test import TestCase
from django.urls import reverse


class CoreViewsTests(TestCase):
    def test_index_renders_landing_page(self):
        response = self.client.get(reverse("core:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/index.html")
        self.assertContains(response, "Vercel + Supabase")

    def test_health_returns_ok_json(self):
        response = self.client.get(reverse("core:health"))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"app": "core", "status": "ok"})
