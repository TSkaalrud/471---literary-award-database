from django.urls import path,include
from django.db import models
from . import views
urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('authors/', views.AuthorList.as_view()),
    path('authors/<int:pk>', views.AuthorDetail.as_view()),
    path('pubWorks/', views.PubWorkList.as_view()),

    path('works/', views.WorkList.as_view()),
    path('works/<int:AuthorName>/<slug:PublisherName>/<slug:WorkName>', views.WorkDetail.as_view()),
    path('thirdParties/', views.ThirdPartyList.as_view()),
    path('thirdParties/<int:pk>', views.ThirdPartyDetail.as_view()),
    path('pubs/', views.PublicationList.as_view()),
    path('pubs/<slug:PublisherName>/<int:AuthorName>', views.PublicationDetail.as_view()),    
    path('publishers/', views.PublisherList.as_view()),
    path('publishers/<int:pk>', views.PublisherDetails.as_view()),
    path('litAwards/', views.LiteraryAwardList.as_view()),
    path('litAwards/<int:NominatorName>/<slug:DonorName>', views.LiteraryAwardDetail.as_view()),
    path('donors/', views.DonorList.as_view()),
    path('donors/<int:pk>', views.DonorDetails.as_view()),
    path('awardsBasedC/', views.AwardBasedList.as_view()),
    
    path('mutExclusivityL/', views.MEListList.as_view()),

    path('worksBasedC/', views.WorkBasedList.as_view()),

    path('authorsBasedC/', views.AuthorBasedList.as_view()),

    path('vendors/', views.VendorList.as_view()),
    path('vendors/<int:pk>', views.VendorDetails.as_view()),
    path('sales/', views.SellList.as_view()),
    path('sales/<slug:W_Name>/<int:V_Name>', views.SellDetails.as_view()),
    
]
