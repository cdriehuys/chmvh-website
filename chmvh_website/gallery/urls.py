from django.conf.urls import include, url

from gallery import api_views, views


apiurls = [
    url(r'^patients/$', api_views.PetListCreateView.as_view(),
        name='patient-list'),
]


urlpatterns = [
    url(r'^$', views.GalleryIndexView.as_view(), name='index'),
    url(r'^api/', include(apiurls, namespace='api')),
    url(r'^memoriam/$', views.PetMemoriamView.as_view(), name='pet-memoriam'),
    url(r'^search/$', views.PatientSearchView.as_view(), name='search'),
    url(r'^(?P<first_letter>[a-zA-Z])/$', views.PetListView.as_view(),
        name='pet-list'),
]
