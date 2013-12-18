from django.conf.urls import patterns, include, url
from django.contrib import admin
import rest_framework_nested
from rest_framework_nested.routers import SimpleRouter

from sharefood import views
from mysite.routers import DefaultRouter


admin.autodiscover()

router = DefaultRouter()
router.register(r'food_donations', views.DonatedFoodViewSet)
router.register(r'users', views.UserViewSet)

food_donations_router = rest_framework_nested.routers.NestedSimpleRouter(router, r'food_donations',
                                                                         lookup='food_donations')
food_donations_router.register(r'reservations', views.FoodReservationViewSet)

urlpatterns = patterns('',
                       url(r'^api/v1/food/', include(router.urls)),
                       url(r'^api/v1/food/', include(food_donations_router.urls)),
                       url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^admin/', include(admin.site.urls)),
)
