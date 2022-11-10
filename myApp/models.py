from django.contrib.auth.models import User
from django.db import models
# from django.forms import ModelForm
TITLE_CHOICES = [
('MR', 'Mr.'),
('MRS', 'Mrs.'),
('MS', 'Ms.'),
]
class Author(models.Model):
	name = models.CharField(max_length=100)
	title = models.CharField(max_length=3, choices=TITLE_CHOICES)
	birth_date = models.DateField(blank=True, null=True)

	def __str__(self):
		return self.title + ' '+ self.name


class Book(models.Model):
	name = models.CharField(max_length=100)
	authors = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
	date_published = models.DateField(auto_now_add=True)
	context = models.TextField()
	slug = models.SlugField(blank=True, null=True, default='a')
	picture = models.ImageField(blank=True, upload_to="media")
	reader = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

	def __str__(self):
		return self.name

	def snip(self):
		return self.context[:50] + str('...')