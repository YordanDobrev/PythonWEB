from django.contrib.auth import get_user_model
from django.views.generic import ListView
from Artonia_v2.art_painting.models import ArtPainting
from Artonia_v2.macrame.models import Macrame

UserModel = get_user_model()


class PublicArtworkListView(ListView):
    model = Macrame, ArtPainting
    template_name = 'artwork/public_artwork_list.html'
    context_object_name = 'macrames'
    paginate_by = 12

    def get_queryset(self):
        queryset = Macrame.objects.filter(is_public=True).order_by('-created_at')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        public_macrames = Macrame.objects.select_related('user').filter(is_public=True).order_by('-created_at')
        public_arts = ArtPainting.objects.select_related('user').filter(is_public=True).order_by('-created_at')

        macrames_by_creator = {}
        arts_by_creator = {}

        for macrame in public_macrames:
            creator_username = macrame.user.username
            if creator_username not in macrames_by_creator:
                macrames_by_creator[creator_username] = []
            macrames_by_creator[creator_username].append(macrame)
        context['macrames_by_creator'] = macrames_by_creator

        for art in public_arts:
            creator_username = art.user.username
            if creator_username not in arts_by_creator:
                arts_by_creator[creator_username] = []
            arts_by_creator[creator_username].append(art)
        context['arts_by_creator'] = arts_by_creator

        return context

#
# class ArtworkDetailView(DetailView):
#     model = Artwork
#     template_name = 'artwork/artwork_detail.html'
#     context_object_name = 'artwork'
#     slug_url_kwarg = 'slug'
#
#     def get(self, request, *args, **kwargs):
#         response = super().get(request, *args, **kwargs)
#         if not request.session.get(f'artwork_viewed_{self.object.id}'):
#             self.object.views_count += 1
#             self.object.save()
#             request.session[f'artwork_viewed_{self.object.id}'] = True
#         return response
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['comments'] = self.object.comments.all()[:10]
#         context['is_liked'] = False
#         if self.request.user.is_authenticated:
#             context['is_liked'] = self.object.likes.filter(id=self.request.user.id).exists()
#         return context
#
# #
# @login_required
# def toggle_artwork_like(request, slug):
#     artwork = get_object_or_404(Artwork, slug=slug)
#     is_liked = artwork.likes.filter(id=request.user.id).exists()
#     #
#     if is_liked:
#         artwork.likes.remove(request.user)
#         liked = False
#     else:
#         artwork.likes.add(request.user)
#         liked = True
#
#     return JsonResponse({
#         'liked': liked,
#         'like_count': artwork.like_count
#     })
# #
# #
# @login_required
# def share_artwork(request, slug):
#     if request.method == 'POST':
#         artwork = get_object_or_404(Artwork, slug=slug)
#         share_message = request.POST.get('share_message', '')
#
#         ArtworkShare.objects.create(
#             artwork=artwork,
#             shared_by=request.user,
#             share_message=share_message
#         )
#
#         return JsonResponse({
#             'status': 'success',
#             'message': 'Artwork shared successfully'
#         })
#
#     return JsonResponse({
#         'status': 'error',
#         'message': 'Invalid request method'
#     })
