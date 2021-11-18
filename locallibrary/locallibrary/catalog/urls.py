from django.conf.urls import url

from . import views


urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^books/$', views.BookListView.as_view(), name='books'),#as_view es un metodo de clase
#Uso de patron, Por ejemplo, esto coincidiría con book/1234, y enviaría una variable pk='1234' a la vista.
url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'), 

url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'), 
#url('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]

urlpatterns += [
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    url(r'^borrowed/$', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),  # Added for challenge
]

#URL para la página de renovar libros.
urlpatterns += [
    url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
]

#para crear, editar y eliminar registros de Author de nuestra libreria
urlpatterns += [
    url(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    url(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    url(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
]


# Add URLConf to create, update, and delete books
urlpatterns += [
    url(r'^book/create/$', views.BookCreate.as_view(), name='book-create'),
    url(r'^book/(?P<pk>\d+)/update/$', views.BookUpdate.as_view(), name='book-update'),
    url(r'^book/(?P<pk>\d+)/delete/$', views.BookDelete.as_view(), name='book-delete'),
]