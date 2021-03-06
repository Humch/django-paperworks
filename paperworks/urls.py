from django.conf.urls import url, include

from django.conf import settings

from .views import PapermailList, PapermailDetail, PapermailCreate, PapermailUpdate, PapermailDelete, SenderCreate, RecipientCreate, PrivatePapermailMedia

from auxiliare import urls

urlpatterns = [
    url(r'^', include('auxiliare.urls')),
    url(r'^list/$', PapermailList.as_view(), name='papermail-list'),
    url(r'^(?P<pk>\d+)/$', PapermailDetail.as_view(), name='papermail-detail'),
    url(r'^create/$', PapermailCreate.as_view(), name='papermail-create'),
    url(r'^maj/(?P<pk>\d+)/$', PapermailUpdate.as_view(), name='papermail-update'),
    url(r'^delete/(?P<pk>\d+)/$', PapermailDelete.as_view(), name='papermail-delete'),
    url(r'^create-sender/$', SenderCreate.as_view(), name='sender-create'),
    url(r'^create-recipient/$', RecipientCreate.as_view(), name='recipient-create'),
    url(r'^download-papermail/(?P<pk>\d+)/$', PrivatePapermailMedia.as_view(), name='private-papermail-media'),
]
