from django.conf.urls import patterns, include, url
from django.contrib import admin
import rest_framework_nested
from rest_framework_nested.routers import SimpleRouter

from sharefood import views
from mysite.routers import DefaultRouter


admin.autodiscover()

donations_router = DefaultRouter()
donations_router.register(r'donations', views.DonatedFoodViewSet)

users_router = SimpleRouter()
users_router.register(r'users', views.UserViewSet)

food_donations_router = rest_framework_nested.routers.NestedSimpleRouter(donations_router, r'donations',
                                                                         lookup='donations')
food_donations_router.register(r'reservations', views.FoodReservationViewSet)

urlpatterns = patterns('',
                       url(r'^api/v1/', include(users_router.urls)),
                       url(r'^api/v1/food/', include(donations_router.urls)),
                       url(r'^api/v1/food/', include(food_donations_router.urls)),
                       url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^admin/', include(admin.site.urls)),
)
