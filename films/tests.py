from django.test import TestCase
from django.urls import reverse
from films.models import Film

def add_film(name, short_name = "", icon_uri = ""):
    data = {
        "name": name,
        "short_name": short_name,
        "icon_uri": icon_uri,
        "extra_field": "some value",
    }
    return Film.objects.create(name=name, short_name=short_name, icon_uri=icon_uri, data=data)


class FilmsIndexViewTests(TestCase):
    def test_no_films(self):
        """
        If there are no films in database, an appropriate message is displayed.
        """
        response = self.client.get(reverse("films:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No films are available")
        self.assertQuerySetEqual(response.context["film_list"], [])

    def test_single_film(self):
        """
        Database with single film is properly displayed
        """
        film = add_film("Long film name", "Short name", icon_uri="https://example.com/image.jpg")
        response = self.client.get(reverse("films:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Short name")
        self.assertQuerySetEqual(response.context["film_list"], [film])

    def test_two_films(self):
        """
        Database with two films is properly displayed
        """
        film1 = add_film("Long film name", "Short name", icon_uri="https://example.com/image.jpg")
        film2 = add_film("Another long film name", icon_uri="https://example.com/image.jpg")
        response = self.client.get(reverse("films:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Short name")
        self.assertContains(response, "Another long film name")
        self.assertQuerySetEqual(response.context["film_list"], [film1, film2], ordered=False)
