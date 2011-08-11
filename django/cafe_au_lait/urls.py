from django.conf.urls.defaults import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^home/$', 'menu.views.index'),	    

	(r'^orders/submit/$', 'orders.views.submit'),
	(r'^orders/current/$', 'orders.views.current'),

    url(r'^admin/', include(admin.site.urls)),
)
