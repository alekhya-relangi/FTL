from rest_framework import serializers

from .models import members

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = members
        fields = ('m_id', 'real_name','tz','start_time','end_time')
        
