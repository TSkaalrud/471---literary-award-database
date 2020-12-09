from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .serializers import AuthorSerializer
from .serializers import PubWorkSerializer
from .serializers import WorkSerializer
from .serializers import ThirdPartySerializer
from .serializers import PublicationSerializer
from .serializers import PublisherSerializer
from .serializers import LiteraryAwardSerializer
from .serializers import DonorSerializer
from .serializers import AwardBasedSerializer
from .serializers import MEListSerializer
from .serializers import WorkBasedSerializer
from .serializers import AuthorBasedSerializer
from .serializers import VendorSerializer
from .serializers import SellSerializer
from .models import User
from .models import Author
from .models import PubWork
from .models import Work
from .models import ThirdParty
from .models import Publication
from .models import Publisher
from .models import LiteraryAward
from .models import Donor
from .models import AwardBased
from .models import MEList
from .models import WorkBased
from .models import AuthorBased
from .models import Vendor
from .models import Sell

class UserList (APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer (users, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail (APIView):

    def get(self, request, pk, format=None):
        user = User.objects.get (pk=pk)
        serializer = UserSerializer(user)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        user = User.objects.filter(pk=pk).first()
        serializer = UserSerializer(user, data=request.data)
        print(user)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = User.objects.filter (pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorList (APIView):
    #Viewing all Authors
    def get(self, request, format=None):
        authors = Author.objects.all()
        serializer = AuthorSerializer (authors, many=True)
        return Response (serializer.data)

    #Adding new Author
    def post(self, request, format=None):
        serializer = AuthorSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class AuthorDetail(APIView):
    #Searching Author Based on Author Name
    def get(self, request, AuthorName, format=None):
        author = Author.objects.get (AuthorName=AuthorName)
        serializer = AuthorSerializer(author)
        return Response (serializer.data)

    #Updating information of existing author
    def put(self, request, AuthorName, format=None):
        author = Author.objects.filter(AuthorName=AuthorName).first()
        serializer = AuthorSerializer(author, data=request.data)
        print(author)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Deleting an Author
    def delete(self, request, AuthorName, format=None):
        author = Author.objects.filter (AuthorName=AuthorName)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PubWorkList (APIView):
    #Viewing all published works of the author
    def get(self, request, format=None):
        works = PubWork.objects.all()
        serializer = PubWorkSerializer (works, many=True)
        return Response (serializer.data)
    
    #Adding a new published work of the author
    def post(self, request, format=None):
        serializer = PubWorkSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkList (APIView):
    #Viewing all Works
    def get(self, request, format=None):
        work = Work.objects.all()
        serializer = WorkSerializer (work, many=True)
        return Response (serializer.data)

    #New Work 
    def post(self, request, format=None):
        serializer = WorkSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkDetail (APIView):
    #Searching for Work
    def get(self, request, WorkName, format=None):
        work = Work.objects.get (WorkName=WorkName)
        serializer = WorkSerializer(work)
        return Response (serializer.data)
    
    #Updating work
    def put(self, request, WorkName, format=None):
        work = Work.objects.filter(WorkName=WorkName).first()
        serializer = WorkSerializer(work, data=request.data)
        print(work)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Deleting Work
    def delete(self, request, WorkName, format=None):
        work = Work.objects.filter (WorkName=WorkName)
        work.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ThirdPartyList (APIView):
    #Viewing all ThirdParties
    def get(self, request, format=None):
        party = ThirdParty.objects.all()
        serializer = ThirdPartySerializer (party, many=True)
        return Response (serializer.data)

    #Adding new Party
    def post(self, request, format=None):
        serializer = ThirdPartySerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ThirdPartyDetail (APIView):
    #Searching for Party
    def get(self, request, PartyName, format=None):
        party = ThirdParty.objects.get (PartyName=PartyName)
        serializer = ThirdPartySerializer(party)
        return Response (serializer.data)

    #Updating Third Party information
    def put(self, request, PartyName, format=None):
        party = ThirdParty.objects.filter(PartyName=PartyName).first()
        serializer = ThirdPartySerializer(party, data=request.data)
        print(party)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Deleting a Third Party
    def delete(self, request, PartyName, format=None):
        party = ThirdParty.objects.filter (PartyName=PartyName)
        party.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PublicationList (APIView):
    #Viewing all Publications
    def get(self, request, format=None):
        publication = Publication.objects.all()
        serializer = PublicationSerializer (publication, many=True)
        return Response (serializer.data)

    #Adding new Publication
    def post(self, request, format=None):
        serializer = PublicationSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublicationDetail (APIView):
    #Searching for Publication
    def get(self, request, PublisherName, AuthorName, format=None):
        publication = Publication.objects.get (PublisherName=PublisherName,AuthorName=AuthorName)
        serializer = PublicationSerializer(publication)
        return Response (serializer.data)

    #Update existing Publication
    def put(self, request, PublisherName, AuthorName, format=None):
        publication = Publication.objects.filter(PublicationName=PublicationName, AuthorName=AuthorName).first()
        serializer = PublicationSerializer(publication, data=request.data)
        print(publication)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Delete a Publication
    def delete(self, request, PublisherName, AuthorName, format=None):
        publication = Publication.objects.filter (PublisherName=PublisherName, AuthorName=AuthorName)
        publication.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PublisherList (APIView):
    #Viewing all Publishers
    def get(self, request, format=None):
        publisher = Publisher.objects.all()
        serializer = PublisherSerializer (publisher, many=True)
        return Response (serializer.data)

    #Adding new Publisher
    def post(self, request, format=None):
        serializer = PublisherSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublisherDetails (APIView):
    #Searching for Publisher
    def get(self, request, PublisherName, format=None):
        publisher = Publisher.objects.get (PublisherName=PublisherName)
        serializer = PublisherSerializer(publisher)
        return Response (serializer.data)

    #Updating existing Publisher
    def put(self, request, PublisherName, format=None):
        publisher = Publisher.objects.filter(PublisherName=PublisherName).first()
        serializer = PublisherSerializer(publisher, data=request.data)
        print(publisher)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Delete a Publisher
    def delete(self, request, PublisherName, format=None):
        publisher = Publisher.objects.filter (PublisherName=PublisherName)
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LiteraryAwardList(APIView):
    #Viewing All Literary Awards
    def get(self, request, format=None):
        litAward = LiteraryAward.objects.all()
        serializer = LiteraryAwardSerializer (litAward, many=True)
        return Response (serializer.data)
    
    #Adding New Literary Award
    def post(self, request, format=None):
        serializer = LiteraryAwardSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LiteraryAwardDetail(APIView):
    #Searching Literary Award
    def get(self, request, NominatorName, DonorName, format=None):
        litAward = LiteraryAward.objects.get (NominatorName=NominatorName, DonorName=DonorName)
        serializer = LiteraryAwardSerializer(litAward)
        return Response (serializer.data)

    #Updating existing Literary Award
    def put(self, request, NominatorName, DonorName, format=None):
        litAward = LiteraryAward.objects.filter(NominatorName=NominatorName, DonorName=DonorName).first()
        serializer = LiteraryAwardSerializer(litAward, data=request.data)
        print(litAward)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Deleting a Literary Award
    def delete(self, request, NominatorName, DonorName, format=None):
        litAward = LiteraryAward.objects.filter (NominatorName = NominatorName, DonorName = DonorName)
        litAward.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DonorList (APIView):
    #Viewing All Donors
    def get(self, request, format=None):
        donor = Donor.objects.all()
        serializer = DonorSerializer (donor, many=True)
        return Response (serializer.data)

    #Adding new Donor
    def post(self, request, format=None):
        serializer = DonorSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DonorDetails (APIView):
    #Searching for Donor
    def get(self, request, Name, format=None):
        donor = Donor.objects.get (Name=Name)
        serializer = DonorSerializer(litAward)
        return Response (serializer.data)

    #Updating existing Donor
    def put(self, request, Name, format=None):
        donor = Donor.objects.filter(Name = Name).first()
        serializer = DonorSerializer(donor, data=request.data)
        print(litAward)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Deleting a Donor
    def delete(self, request, Name, format=None):
        donor = Donor.objects.filter (Name = Name)
        donor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AwardBasedList (APIView):
    #Viewing All Award Based Awards
    def get(self, request, format=None):
        AB = AwardBased.objects.all()
        serializer = AwardBasedSerializer (AB, many=True)
        return Response (serializer.data)

    #Adding new Award Based Awards
    def post(self, request, format=None):
        serializer = AwardBasedSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MEListList (APIView):
    #Viewing List
    def get(self, request, format=None):
        Mlist = MEList.objects.all()
        serializer = MEListSerializer (MList, many=True)
        return Response (serializer.data)

    #Adding new List
    def post(self, request, format=None):
        serializer = MEListSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkBasedList (APIView):
    #View All Work Based Awards
    def get(self, request, format=None):
        WB = WorkBased.objects.all()
        serializer = WorkBasedSerializer (WB, many=True)
        return Response (serializer.data)

    #Adding new Award Based Awards
    def post(self, request, format=None):
        serializer = WorkBasedSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorBased (APIView):
    #Viewing All Author Based Awards
    def get(self, request, format=None):
        AB = AuthorBased.objects.all()
        serializer = AuthorBasedSerializer (AB, many=True)
        return Response (serializer.data)

    #Adding new Award Based Awards
    def post(self, request, format=None):
        serializer = AuthorBasedSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorList (APIView):
    #Viewing All Vendors
    def get(self, request, format=None):
        vendor = Vendor.objects.all()
        serializer = VendorSerializer (vendor, many=True)
        return Response (serializer.data)

    #Adding new Award Based Awards
    def post(self, request, format=None):
        serializer = VendorSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorDetails (APIView):
    #Searching for Vendor
    def get(self, request, Name, format=None):
        vendor = Vendor.objects.get (Name=Name)
        serializer = VendorSerializer(vendor)
        return Response (serializer.data)

    #Updating existing Vendor
    def put(self, request, Name, format=None):
        vendor = Vendor.objects.filter(Name = Name).first()
        serializer = VendorSerializer(vendor, data=request.data)
        print(vendor)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Deleting a Vendor
    def delete(self, request, Name, format=None):
        vendor = Vendor.objects.filter (Name = Name)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SellList (APIView):
    #Viewing All Sales
    def get(self, request, format=None):
        sell = Sell.objects.all()
        serializer = SellSerializer (sell, many=True)
        return Response (serializer.data)

    #Adding new Sales
    def post(self, request, format=None):
        serializer = SellSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SellDetails (APIView):
    #Searching for Sale
    def get(self, request, W_Name, V_Name, format=None):
        sell = Sell.objects.get (W_Name=W_Name, V_Name = V_Name)
        serializer = SellSerializer(sell)
        return Response (serializer.data)

    #Updating existing Sale
    def put(self, request, W_Name, V_Name, format=None):
        sell = Sell.objects.filter(W_Name = W_Name, V_Name = V_Name).first()
        serializer = SellSerializer(sell, data=request.data)
        print(sell)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Deleting a Sale
    def delete(self, request, W_Name, V_Name, format=None):
        sell = Sell.objects.filter (W_Name = W_Name, V_Name = V_Name)
        sell.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
