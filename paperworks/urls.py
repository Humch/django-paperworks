from django.conf.urls import url

from .views import PapermailList, PapermailDetail, PapermailCreate, PapermailUpdate, PapermailDelete

urlpatterns = [
    url(r'^$', PapermailList.as_view(), name='papermail-list'),
    url(r'^(?P<pk>\d+)/$', PapermailDetail.as_view(), name='papermail-detail'),
    url(r'^create/$', PapermailCreate.as_view(), name='papermail-create'),
    url(r'^maj/(?P<pk>\d+)/$', PapermailUpdate.as_view(), name='papermail-update'),
    url(r'^delete/(?P<pk>\d+)/$', PapermailDelete.as_view(), name='papermail-delete'),
]
