"""Код описывает модель данных для создания объектов блога в Django"""
from django.db import models
from django.conf import settings
from django.utils import timezone

"""Cекция выше импортирует необходимые модули Django для работы с базой данных, настройками проекта и временными метками"""

class Post(models.Model):   # Эта строка создает новую модель Post (объект блога) и указывает, что она наследуется от базовой модели Django models.Model.
	"""Cтрока ниже создает поле author в модели Post, которое связывает каждый пост с пользователем, используя внешний ключ ForeignKey.
	 settings.AUTH_USER_MODEL ссылается на модель пользователей, определенную в проекте.
	 on_delete=models.CASCADE указывает, что при удалении пользователя, все связанные с ним посты также должны быть удалены."""
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)    # blank=True позволяет полю быть пустым, а null=True разрешает полю принимать значение NULL.
	
	def publish(self):  # Этот метод publish определяет дату и время публикации поста и сохраняет его в базу данных.
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.title