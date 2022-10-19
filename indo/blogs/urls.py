from django.urls import path, reverse_lazy
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.BlogListView.as_view(), name='blogs_list'),
    path('blogs/<int:pk>', views.BlogDetailView.as_view(), name='blogs_detail'),
    path('blogs/create', views.BlogCreateView.as_view(success_url=reverse_lazy('blogs:blogs_list')), name='blogs_create'),
    path('blogs/<int:pk>/update', views.BlogUpdateView.as_view(success_url=reverse_lazy('blogs:blogs_list')), name='blogs_update'),
    path('blogs/<int:pk>/delete', views.BlogDeleteView.as_view(success_url=reverse_lazy('blogs:blogs_list')), name='blogs_delete'),
]