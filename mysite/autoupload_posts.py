import sys
import os

# a nasty hack to set up correct settings module
old_django_settings = os.environ.get("DJANGO_SETTINGS_MODULE", None)
os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"

from django.utils import timezone
from django_summernote.models import Attachment
from django.core.files import File
from django.conf import settings
from posts.models import Post

IMG_HTML = "<img class='img-responsive' src='{}' />"
TEXT_HTML = "<p>{}</p>"


class UploadException(Exception):
    pass


def main():
    if len(sys.argv) < 2:
        raise UploadException("Data dir should come as a param")
    data_dir = sys.argv[1]
    for post_dir_name in os.listdir(data_dir):
        # post dir name has format postid_pubdate
        text = ""

        def _get_path(filename=''):
            return os.path.join(data_dir, post_dir_name, filename)
        pics = [f for f in os.listdir(_get_path()) if f != 'text']
        with open(_get_path('text')) as post_text:
            text = TEXT_HTML.format(post_text.read())
        [post_id, seconds] = map(lambda x: int(x), post_dir_name.split('_'))
        pubdate = timezone.datetime.utcfromtimestamp(seconds)
        # now add TZ info. We save everything in UTC so TZ=utc
        pubdate = timezone.make_aware(pubdate, timezone.utc)
        title = "auto uploaded post {}".format(post_id)
        add_br = False
        for pic in pics:
            add_br = not(pic not in [pics[0], pics[-1]]) or True
            # upload attachments
            attachment = Attachment(name=pic,
                                    file=File(open(_get_path(pic), 'rb')))
            attachment.save()
            # insert pics in text
            if add_br:
                text += "<br/>"
            text += IMG_HTML.format(os.path.join(settings.MEDIA_URL,
                                                 attachment.file.name))
        post = Post(title=title, text=text, pub_date=pubdate)
        post.save()


if __name__ == "__main__":
    main()
    # restore settings
    if old_django_settings:
        os.environ["DJANGO_SETTINGS_MODULE"] = old_django_settings
