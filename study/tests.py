from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate

from study.models import Course, Lesson, Subscribe
from users.models import User


class StudyTestCase(APITestCase):

    def setUp(self):
        super().setUp()

        self.user = User.objects.create(
            email='admin3@sky.pro',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        self.course = Course.objects.create(title = "TestListCourse")

        self.lesson = Lesson.objects.create(
            title = "TestList",
            course = self.course,
            url_link ="youtube.com",
            owner = self.user
        )

        self.client.force_authenticate(user=self.user)


    def test_list_lesson(self):
        """ Тестирование вывода списка уроков """
        

        response = self.client.get(
            reverse('study:lesson_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1, 
             'next': None, 
             'previous': None, 
             'results':[
                    {
                    "id": self.lesson.pk, 
                    "title": self.lesson.title,
                    "descriprion": None, 
                    "preview": None, 
                    "course": self.lesson.course.pk, 
                    "url_link": self.lesson.url_link, 
                    "owner": self.user.pk
                    }
                ]
            }
        )

    def test_create_lesson(self):
        """ Тестирования создания урока """

        data = {
            "title": "TestList34",
            "course": self.course.pk,
            "url_link": "youtube.com"
        }

        response = self.client.post(
            reverse('study:lesson_create'),
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Lesson.objects.all().count(),
            2
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_update_lesson(self):
        """ Тестирование обновления урока """

        data = {
            "title": "TestLesson2"
        }

        response = self.client.patch(
            reverse('study:lesson_update', args=(self.lesson.pk,)),
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.lesson.refresh_from_db()

        self.assertEqual(
            self.lesson.title,
            "TestLesson2"
        )

    def test_retrieve_lesson(self):
        """ Тестирование извлечения урока """

        url = reverse("study:lesson_get", args=(self.lesson.pk,))

        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            data.get("title"),
            self.lesson.title
        )

    def test_delete_lesson(self):
        """ Тестирование удаления урока """

        response = self.client.delete(
            reverse('study:lesson_delete', args=(self.lesson.pk,))            
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Lesson.objects.all().count(),
            0
        )


    def test_subscribe(self):
        data = {
            "course": self.course.pk
        }

        response = self.client.post(
            '/course/subscribe/',
            data=data
        )

        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, {'message': 'Подписка включена'})

    def test_unsubscribe(self):
        data = {
            "course": self.course.pk
        }

        Subscribe.objects.create(course=self.course, user=self.user)

        response = self.client.post(
            '/course/subscribe/',
            data=data
        )
        
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, {'message': 'Подписка отключена'})