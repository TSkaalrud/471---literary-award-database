from django.urls import path,include
from . import views
urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('authors/', views.AuthorList.as_view()),
    path('authors/<int:pk>', views.AuthorDetail.as_view()),
    path('pubWorks/', views.PubWorkList.as_view()),

    path('works/', views.WorkList.as_view()),
    path('works/<int:pk>', views.WorkDetail.as_view()),
    path('thirdParties/', views.ThirdPartyList.as_view()),
    path('thirdParties/<int:pk>', views.ThirdPartyDetail.as_view()),
    path('pubs/', views.PublicationList.as_view()),
    path('pubs/<int:pk>', views.PublicationDetail.as_view()),    
    path('publishers/', views.PublisherList.as_view()),
    path('publishers/<int:pk>', views.PublisherDetails.as_view()),
    path('litAwards/', views.LiteraryAwardList.as_view()),
    path('litAwards/<int:pk>', views.LiteraryAwardDetail.as_view()),
    path('donors/', views.DonorList.as_view()),
    path('donors/<int:pk>', views.DonorDetails.as_view()),
    path('awardsBasedC/', views.AwardBasedList.as_view()),
    
    path('mutExclusivityL/', views.MEListList.as_view()),

    path('worksBasedC/', views.WorkBasedList.as_view()),

    path('authorsBasedC/', views.AuthorBased.as_view()),

    path('vendors/', views.VendorList.as_view()),
    path('vendors/<int:pk>', views.VendorDetails.as_view()),
    path('sales/', views.SellList.as_view()),
    path('sales/<int:pk>', views.SellDetails.as_view()),
    
]
