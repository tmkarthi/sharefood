from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets

from sharefood.models import DonatedFood
from sharefood.permissions import IsDonorOrReadOnly
from sharefood.serializers import DonatedFoodSerializer, UserSerializer


class DonatedFoodViewSet(viewsets.ModelViewSet):
    """
This endpoint presents code sharefood.

The `highlight` field presents a hyperlink to the hightlighted HTML
representation of the code snippet.

The **owner** of the code snippet may update or delete instances
of the code snippet.

Try it yourself by logging in as one of these four users: **amy**, **max**,
**jose** or **aziz**. The passwords are the same as the usernames.
"""
    queryset = DonatedFood.objects.all()
    serializer_class = DonatedFoodSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsDonorOrReadOnly,)

    # @link(renderer_classes=(renderers.StaticHTMLRenderer,))
    # def highlight(self, request, *args, **kwargs):
    #     snippet = self.get_object()
    #     return Response(snippet.highlighted)

    def pre_save(self, obj):
        obj.donor = self.request.user


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
This endpoint presents the users in the system.

As you can see, the collection of snippet instances owned by a user are
serialized using a hyperlinked representation.
"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = 'username'