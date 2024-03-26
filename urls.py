
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from dappx import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dappx.views import patient_view, testing_view, about_page_view, testing_list_view, testing_detail_view, testing_delete_view, testing_update_view, testing_create_view, patient_list_view, patient_detail_view, patient_delete_view, patient_update_view, patient_create_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('details/', patient_view, name='patient'),
    path('data/', testing_view, name='test'),
    path('list/', testing_list_view, name='testing_list'),
    path('create/', testing_create_view, name='testing-list'),
    path('list/<int:id>/', testing_detail_view, name='testing_detail'),
    path('<int:id>/update/', testing_update_view, name='testing-update'),
    path('<int:id>/delete/', testing_delete_view, name='testing-delete'),
    path('plist/', patient_list_view, name='patient_list'),
    path('pcreate/', patient_create_view, name='patient-list'),
    path('plist/<int:id>/', patient_detail_view, name='patient_detail'),
    path('<int:id>/pupdate/', patient_update_view, name='patient-update'),
    path('<int:id>/pdelete/', patient_delete_view, name='patient-delete'),
    url(r'^$', views.index, name='index'),
    url('data/', views.iotdata_view, name='iotdata'),
    url(r'^details/', views.iotdetails_view, name='iotdetails'),
    url(r'^special/', views.special, name='special'),
    url(r'^dappx/', include('dappx.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^about/', views.about_page_view, name='about'),

]

urlpatterns+=staticfiles_urlpatterns()