from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
     url(r'^$',views.home,name='home'),
    url(r'camden/project/(\d+)',views.rate_project,name='rate-project'),
    url(r'camden/profile',views.view_profile,name='view-profile'),
    url(r'^search/', views.search_project, name='search_project'),
    url(r'^new/project$', views.new_project, name='new_project'),
    url(r'^camdenapi/api/profile/$', views.ProfileList.as_view(),name='api-profile'),
    url(r'^camdenapi/api/project/$', views.ProjectList.as_view(),name='api-project'),
    url(r'^camdenapi/$',views.api_page,name='api-page'),
    url('register/',views.register, name='register'),
    
]
