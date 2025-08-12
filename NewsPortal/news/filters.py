from django_filters import FilterSet
from .models import Post

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
   class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
           'time_creation': ['gt'],
           'author': ['exact'],  # фильтр по автору, что выбрал пользователь
       }
