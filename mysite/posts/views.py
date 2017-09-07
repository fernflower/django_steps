import json

from django.conf import settings
from django import http
from django.views import generic

import forms


class IndexView(generic.TemplateView):
    template_name = 'posts/index.html'
    send_to_list = ['inavasilevskaya@gmail.com']

    def get_context_data(self, **kwargs):
        block = int(self.request.GET.get('block', 0))
        n = int(self.request.GET.get('videos', settings.VIDEOS_PER_BLOCK))
        videos = self.get_videos(n, block)
        context = super(IndexView, self).get_context_data(**kwargs)
        context['videos'] = videos
        return context

    @staticmethod
    def get_videos(videos_num, block, filename=settings.VIDEOS_FILE):
        """Retrieve videos_num videos from given block from videos_file"""
        with open(filename, 'r') as f:
            # fields are id/url/name/date
            res = []
            video_data = [l.strip() for l in f.readlines()
                          if l.strip() != ""][block * videos_num:
                                              (block + 1) * videos_num]
            for line in video_data:
                fields = line.split('|')
                if len(fields) > 0:
                    video_id = fields[0].split('/')[-1]
                    fields = [video_id] + fields
                    res.append(fields)
            return res

    @staticmethod
    def get_videos_as_json(request):
        num = int(request.GET.get('n', settings.VIDEOS_PER_BLOCK))
        block = int(request.GET.get('block', 0))
        data = {'videos': IndexView.get_videos(num, block)}
        return http.HttpResponse(json.dumps(data),
                                 content_type="application/json")


class ContactFormView(generic.edit.FormView):
    form_class = forms.ContactForm

    def form_valid(self, form):
        form.send_email()
        return http.HttpResponse("Message sent!")
