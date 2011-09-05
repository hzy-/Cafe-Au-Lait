from django.conf.urls.defaults import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#home page
	(r'^home/$', 'menu.views.index'),	    

	#orders pages
	(r'^orders/submit/$', 'orders.views.submit'),
	(r'^orders/current/$', 'orders.views.current'),
	(r'^orders/clear/$', 'orders.views.clear'),

	#beverage page(s)
	(r'^beverages/list/$', 'beverages.views.list'),

    url(r'^admin/', include(admin.site.urls)),
)
