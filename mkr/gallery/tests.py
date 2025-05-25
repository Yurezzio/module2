from django.test import TestCase
from .models import Category, Image
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date

class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name="Природа")
        self.assertEqual(str(category), "Природа")
        self.assertEqual(Category.objects.count(), 1)

class ImageModelTest(TestCase):
    def setUp(self):
        self.category_mountains = Category.objects.create(name="Гори")
        self.category_sea = Category.objects.create(name="Море")

    def test_create_image_with_multiple_categories(self):
        
        test_image = SimpleUploadedFile(
            "image.jpg",
            b"\x47\x49\x46\x38\x39\x61", 
            content_type="image/jpeg"
        )

        image = Image.objects.create(
            title="Відпочинок",
            image=test_image,
            created_date=date.today(),
            age_limit=12
        )
        image.categories.set([self.category_mountains, self.category_sea])

        self.assertEqual(str(image), "Відпочинок")
        self.assertEqual(image.categories.count(), 2)
        self.assertEqual(Image.objects.count(), 1)
        self.assertIn(self.category_mountains, image.categories.all())
        self.assertIn(self.category_sea, image.categories.all())

