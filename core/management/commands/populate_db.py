from django.core.management.base import BaseCommand
from core.models import Category

class Command(BaseCommand):
	help = 'Populate the deanslist database with some mock data to display in index.html'

	def _create_categories(self):
		# c_community = Category(name='Community')
		# c_community.save()

		s_school_activities = Category(name='School Activities', parent_category=Category.objects.get(name='Community'))
		s_school_activities.save()

		s_local_news = Category(name='Local News', parent_category=Category.objects.get(name='Community'))
		s_local_news.save()

		s_philanthropy = Category(name='Philanthropy', parent_category=Category.objects.get(name='Community'))
		s_philanthropy.save()

	def handle(self, *args, **options):
		self._create_categories()