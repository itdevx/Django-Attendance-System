from django.http import Http404
from django.shortcuts import get_object_or_404


class SuperUserAccessMixins():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('صفحه مورد نظر یافت نشد')
