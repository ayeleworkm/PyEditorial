from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic, View
from django.db.models import Q

from . import models
from .forms import SearchForm

# contact us page 
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

class Home(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {
            'last_blog': models.Blog.objects.order_by('-pk').filter(publish=True)[:1],
            # 'skills': models.Skill.objects.all(),
            'blogs': models.Blog.objects.order_by('-pk').filter(publish=True)[1:5],
            'videocasts': models.Videocast.objects.order_by('-pk').filter(publish=True)[:4]
        }
        return render(request, self.template_name, context)



class Index(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'last_blog': models.Blog.objects.order_by('-pk').filter(publish=True)[:1],
            # 'skills': models.Skill.objects.all(),
            'blogs': models.Blog.objects.order_by('-pk').filter(publish=True)[1:5],
            'videocasts': models.Videocast.objects.order_by('-pk').filter(publish=True)[:4]
        }
        return render(request, self.template_name, context)



class Search(View):
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        form = SearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            context = {
                'blogs': models.Blog.objects.order_by('-pk').filter(
                    Q(title__icontains=query) | Q(content__icontains=query)
                ),
                'videocasts': models.Videocast.objects.order_by('-pk').filter(
                    Q(title__icontains=query) | Q(content__icontains=query)
                ),
                'podcasts': models.Podcast.objects.order_by('-pk').filter(
                    Q(title__icontains=query) | Q(content__icontains=query)
                )
            }
        else:
            return redirect('content:index')
        return render(request, self.template_name, context)


class BlogCategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = models.BlogCategory
    fields = '__all__'
    success_message = 'Blog category was created successfully'

    def get_success_url(self):
        return reverse('content:blog_category_create')
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('content:index')  # Redirect non-admin users from creating blogs
        return super().dispatch(request, *args, **kwargs)


class Blog(generic.ListView):
    model = models.Blog
    template_name = 'blog_archive.html'


class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = models.Blog
    fields = '__all__'
    success_message = 'Blog was created successfully'

    def get_success_url(self):
        return reverse('content:blog_create')
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('content:index')  # Redirect non-admin users from creating blogs
        return super().dispatch(request, *args, **kwargs)


class BlogArchiveByCategoryPK(generic.ListView):
    model = models.Blog
    template_name = 'blog_archive.html'

    def get_queryset(self):
        return self.model.objects.filter(category=self.kwargs['pk'])


class BlogSingle(generic.DetailView):
    model = models.Blog
    template_name = 'single.html'

    def get_queryset(self):
        return self.model.objects.filter(slug=self.kwargs['slug'])


class VideocastCategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = models.VideocastCategory
    fields = '__all__'
    success_message = 'Video cast category was created successfully'

    def get_success_url(self):
        return reverse('content:videocast_category_create')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('content:index')  # Redirect non-admin users from creating blogs
        return super().dispatch(request, *args, **kwargs)


class Videocast(generic.ListView):
    model = models.Videocast
    template_name = 'videocast_archive.html'


class VideocastCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = models.Videocast
    fields = '__all__'
    success_message = 'Video cast was created successfully'

    def get_success_url(self):
        return reverse('content:videocast_create')
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('content:index')  # Redirect non-admin users from creating blogs
        return super().dispatch(request, *args, **kwargs)


class VideocastArchiveByCategoryPK(generic.ListView):
    model = models.Videocast
    template_name = 'videocast_archive.html'

    def get_queryset(self):
        return self.model.objects.filter(category=self.kwargs['pk'])


class VideocastSingle(generic.DetailView):
    model = models.Videocast
    template_name = 'single.html'

    def get_queryset(self):
        return self.model.objects.filter(slug=self.kwargs['slug'])


class PodcastCategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = models.PodcastCategory
    fields = '__all__'
    success_message = 'Podcast category was created successfully'

    def get_success_url(self):
        return reverse('content:podcast_category_create')
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('content:index')  # Redirect non-admin users from creating blogs
        return super().dispatch(request, *args, **kwargs)


class Podcast(generic.ListView):
    model = models.Podcast
    template_name = 'podcast_archive.html'


class PodcastCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = models.Podcast
    fields = '__all__'
    success_message = 'Podcast was created successfully'

    def get_success_url(self):
        return reverse('content:podcast_create')
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('content:index')  # Redirect non-admin users from creating blogs
        return super().dispatch(request, *args, **kwargs)


class PodArchiveByCategoryPK(generic.ListView):
    model = models.Podcast
    template_name = 'podcast_archive.html'

    def get_queryset(self):
        return self.model.objects.filter(category=self.kwargs['pk'])


class PodSingle(generic.DetailView):
    model = models.Podcast
    template_name = 'single.html'

    def get_queryset(self):
        return self.model.objects.filter(slug=self.kwargs['slug'])


# class SkillCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
#     model = models.Skill
#     fields = '__all__'
#     success_message = 'Skill was created successfully'

#     def get_success_url(self):
#         return reverse('content:skill_create')

#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_staff:
#             return redirect('content:index')  # Redirect non-admin users from creating blogs
#         return super().dispatch(request, *args, **kwargs)




def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"Name: {name}\nEmail: {email}\n\n{message}"

        try:
            send_mail(
                subject=subject,
                message=full_message,
                from_email=email,
                recipient_list=['your-email@gmail.com'],  # Replace with recipient email
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"Error sending message: {e}")

        return redirect("contact")  # Redirect back to the contact page

    return render(request, "contact.html")
