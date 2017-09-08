import json

from django.conf import settings
from django import http
from django.views import generic

import forms


class IndexView(generic.TemplateView):
    template_name = 'posts/index.html'
    send_to_list = ['inavasilevskaya@gmail.com']
    all_videos = None

    def get_context_data(self, **kwargs):
        block = int(self.request.GET.get('block', 0))
        n = int(self.request.GET.get('videos', settings.VIDEOS_PER_BLOCK))
        videos, more = self.get_videos(n, block)
        context = super(IndexView, self).get_context_data(**kwargs)
        context['videos'] = videos
        context['more_videos'] = 'false' if not more else 'true'
        return context

    @staticmethod
    def get_videos(videos_num, block, filename=settings.VIDEOS_FILE):
        """Retrieve videos_num videos from given block

        Returns videos_data and a flag that shows if there are any more videos
        to fetch.

        """
        if IndexView.all_videos is None:
            with open(filename, 'r') as f:
                IndexView.all_videos = [l.strip() for l in f.readlines()
                                        if l.strip() != ""]
        # fields are id/url/name/date
        video_data = IndexView.all_videos[block * videos_num:
                                          (block + 1) * videos_num]
        more_videos = len(IndexView.all_videos[(block + 1) * videos_num:]) > 0
        res = []
        for line in video_data:
            fields = line.split('|')
            if len(fields) > 0:
                video_id = fields[0].split('/')[-1]
                fields = [video_id] + fields
                res.append(fields)
        return res, more_videos

    @staticmethod
    def get_videos_as_json(request):
        num = int(request.GET.get('n', settings.VIDEOS_PER_BLOCK))
        block = int(request.GET.get('block', 0))
        videos, more = IndexView.get_videos(num, block)
        data = {'videos': videos, 'more_videos': 'true' if more else 'false'}
        return http.HttpResponse(json.dumps(data),
                                 content_type="application/json")


class ContactFormView(generic.edit.FormView):
    form_class = forms.ContactForm

    def form_valid(self, form):
        form.send_email()
        return http.HttpResponse("Message sent!")
