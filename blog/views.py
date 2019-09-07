from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import SocialLink
from .models import TopicCategory
from .models import TopicContent
from .models import SiteOption


class index(View):
    home = "index.html"
    def get(self, request):
        return render(request, self.home)

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        
        # Should be placed in all views in site
        context['social'] = SocialLink.objects.all().order_by('pk')
        context['site_option'] = SiteOption.objects.all()
        
        # Topic category and contents
        context['topic_category'] = TopicCategory.objects.all().order_by('order')

        for topic in context['topic_category']:
            topic.contents = TopicContent.objects.filter(topic_category=topic.id).order_by('order')

        # print(context['topic_category'])
        return context