from django.urls import path
from .views import NewsList, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostSearchView, PostCategoryView 
# импортируем наше представление

from .views import subscribe_to_category, unsubscribe_from_category
from .views import AppointmentView

from django.views.decorators.cache import cache_page

#app_name = 'news_app' 

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>/', cache_page(10*5) (PostDetailView.as_view()), name='post_detail'),
    path('edit/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('search/', PostSearchView.as_view(), name='post_search'),
    path('make_app/', AppointmentView.as_view(), name='make_app'),
    path('category/<int:pk>', PostCategoryView.as_view(), name='category'),
    path('subscribe/<int:pk>', subscribe_to_category, name='subscribe'),
    path('unsubscribe/<int:pk>', unsubscribe_from_category, name='unsubscribe'),
]
