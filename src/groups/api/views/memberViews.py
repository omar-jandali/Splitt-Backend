from groups.models import Member
from ..serializers import MemberSerializer
from rest_framework import viewsets

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

# from groups.models import Member
#
# from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
# from rest_framework.generics import DestroyAPIView, UpdateAPIView
#
# from groups.api.serializers import MemberSerializer
#
# class MemberCreateView(CreateAPIView):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer
#
# class MemberListView(ListAPIView):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer
#
# class MemberRetrieveView(RetrieveAPIView):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer
#
# class MemberUpdateView(UpdateAPIView):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer
#
# class MemberDestroyView(DestroyAPIView):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer
