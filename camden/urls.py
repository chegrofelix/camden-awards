from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
     url(r'^$',views.home,name='home'),
    url(r'awwards/project/(\d+)',views.rate_project,name='rate-project'),
    url(r'awwards/profile',views.view_profile,name='view-profile'),
    url(r'^search/', views.search_project, name='search_project'),
    url(r'^new/project$', views.new_project, name='new_project'),
    url(r'^awwardsapi/api/profile/$', views.ProfileList.as_view(),name='api-profile'),
    url(r'^awwardsapi/api/project/$', views.ProjectList.as_view(),name='api-project'),
    url(r'^awwardsapi/$',views.api_page,name='api-page'),
    url('register/',views.register, name='register'),
]
