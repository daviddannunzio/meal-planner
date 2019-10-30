from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from meal_planner.views import index, recipe, export
from meals import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'meal_planner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', index),
    url(r'^recipe/$', recipe),
    url(r'^recipe/export/$', export),
]
