
from django.conf.urls import url
from django.contrib import admin

from movie_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movies/$', views.MovieListAPIView.as_view(), name='movie_list_api_view'),
    url(r'^movies/(?P<pk>\d+)/$', views.MovieDetailAPIView.as_view(), name='movie-detail'),
    url(r'^raters/$', views.RaterListAPIView.as_view(), name='rater_list_api_view'),
    url(r'^raters/(?P<pk>\d+)/$', views.RaterDetailAPIView.as_view(), name='rater-detail'),
    url(r'^ratings/$', views.RatingListAPIView.as_view(), name='rating_list_api_view'),
    url(r'^ratings/(?P<pk>\d+)/$', views.RatingDetailAPIView.as_view(), name='rating_detail_api_view'),
]
