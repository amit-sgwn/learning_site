from django.test import TestCase
from  django.utils import timezone
# Create your tests here.
from .models import Course

class CourseModelTest(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(title="Python Regular Expression",description="Lerning Regular Expression")
        now =timezone.now()
        self.assertLess(course.created_at,now)
