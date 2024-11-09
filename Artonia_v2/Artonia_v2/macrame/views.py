from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from Artonia_v2.common.models import Product
from Artonia_v2.macrame.forms import CreateMacrameForm
from Artonia_v2.macrame.models import Macrame
from Artonia_v2.utils import get_user_obj


# class CreateMacrameView(CreateView):
#     model = Product
#     form_class = CreateMacrameForm
#     template_name = 'macrame/create-art-painting.html'
#     success_url = reverse_lazy('dashboard')
#
#     def form_valid(self, form):
#         form.instance.author = get_user_obj()
#         return super().form_valid(form)


class CreateMacrameView(LoginRequiredMixin, CreateView):
    model = Macrame
    fields = ['name', 'description', 'price', 'image_url', 'difficulty_level', 'knot_type', 'knot_description']
    template_name = 'macrame/create-macrame.html'
    success_url = reverse_lazy('dashboard')
    # login_url = '/login/'  # Add this to specify where to redirect if not logged in

    def form_valid(self, form):
        # Add debugging prints
        print(f"User authenticated: {self.request.user.is_authenticated}")
        print(f"Current user: {self.request.user}")

        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        # Print form errors for debugging
        print(f"Form errors: {form.errors}")
        return super().form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        # Add request debugging
        print(f"Session id: {request.session.session_key}")
        print(f"Request method: {request.method}")
        print(f"User: {request.user}")
        print(f"User authenticated: {request.user.is_authenticated}")
        return super().dispatch(request, *args, **kwargs)