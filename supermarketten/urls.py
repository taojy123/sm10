
from django.conf.urls import patterns, include, url
from views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xxx.views.home', name='home'),
    # url(r'^xxx/', include('xxx.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    ('^$', index),
    ('^index/$', index),

    ('^admin/$', admin),
    ('^admin_login/$', admin_login),

    ('^admin_type/$', admin_type),
    ('^add_type/$', add_type),
    ('^del_type/$', del_type),
    ('^update_type/$', update_type),

    ('^type/(.*)/$', type),
    ('^product/(.*)/$', product),

    ('^admin_product/$', admin_product),
    ('^add_product/$', add_product),
    ('^del_product/$', del_product),
    ('^update_product/$', update_product),

    ('^admin_order/$', admin_order),
    ('^del_order/$', del_order),
    ('^check_order/$', check_order),


    ('^cart/$', cart),
    ('^addtocart/(.*)/(.*)/$', addtocart),
    ('^delcart/(.*)/$', delcart),

    ('^addtoorder/(.*)/(.*)/$', addtoorder),
    ('^carttoorder/$', carttoorder),
    ('^submit_order/', submit_order),

    ('^add_comment/$', add_comment),
    ('^del_comment/$', del_comment),

    ('^order_search/$', order_search),

    ('^urge/$', urge),
    ('^cancel/$', cancel),

    ('^thumbnail/$', thumbnail),

    ('^remind/$', remind),

)
# This will work if DEBUG is True
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
