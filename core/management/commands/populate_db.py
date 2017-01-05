from django.core.management.base import BaseCommand
from core.models import Category
import os
import json

class Command(BaseCommand):
	help = 'Populate the deanslist database with some mock data to display in index.html'

	def _create_categories(self):
		with open('categories.json', 'r') as categories_file:
			categories_json = json.load(categories_file)

			for category in categories_json:
				category_name = list(category.keys())[0]
				some_category = Category(name=category_name)
				print('Adding category %s' % category_name)
				some_category.save()

				for subcategory_name in category[category_name]:
					some_subcategory = Category(name=subcategory_name, parent_category=some_category)
					print('\tAdding subcategory %s' % subcategory_name)
					some_subcategory.save()

	def handle(self, *args, **options):
		self._create_categories()