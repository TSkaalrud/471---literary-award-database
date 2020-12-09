from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'

class PubWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PubWork
        fields = '__all__'

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Work
        fields = '__all__'

class ThirdPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ThirdParty
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publication
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = '__all__'

class LiteraryAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LiteraryAward
        fields = '__all__'

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Donor
        fields = '__all__'

class AwardBasedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AwardBased
        fields = '__all__'

class MEListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MEList
        fields = '__all__'

class WorkBasedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkBased
        fields = '__all__'

class AuthorBasedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuthorBased
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = '__all__'

class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sell
        fields = '__all__'

