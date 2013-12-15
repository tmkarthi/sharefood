from sharefood import views
from django.conf.urls import patterns, include, url

from django.contrib import admin
from rest_framework.routers import DefaultRouter

admin.autodiscover()

router = DefaultRouter()
router.register(r'food/donations', views.DonatedFoodViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^admin/', include(admin.site.urls)),
)
