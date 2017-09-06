from django.conf import settings
from django import http
from django.views import generic

import forms


class IndexView(generic.TemplateView):
    template_name = 'posts/index.html'
    send_to_list = ['inavasilevskaya@gmail.com']

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        n = int(self.request.GET.get('videos', settings.VIDEOS_PER_BLOCK))
        blocks = int(self.request.GET.get('blocks', 1))
        videos = self.get_videos(n * blocks)
        context['videos'] = videos
        return context

    def get_videos(self, videos_num, filename=settings.VIDEOS_FILE):
        """Retrieve first videos_num videos data from videos_file"""
        with open(filename, 'r') as f:
            # fields are url/name/date/id
            res = []
            # fetch first n * total_blocks videos from videos_file
            video_data = [l.strip() for l in f.readlines()
                          if l.strip() != ""][:videos_num]
            for line in video_data:
                fields = line.split('|')
                if len(fields) > 0:
                    video_id = fields[0].split('/')[-1]
                    fields = [video_id] + fields
                    res.append(fields)
            return res


class ContactFormView(generic.edit.FormView):
    form_class = forms.ContactForm

    def form_valid(self, form):
        form.send_email()
        return http.HttpResponse("Message sent!")
