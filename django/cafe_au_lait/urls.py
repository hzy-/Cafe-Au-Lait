from django.conf.urls.defaults import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
	(r'^orders/submit/$', 'orders.views.submit'),
	(r'^home/$', 'menu.views.index'),	

    url(r'^admin/', include(admin.site.urls)),
)
