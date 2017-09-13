import functools
import gettext
import json

from babel import support
import bottle
import jinja2

VIDEOS_FILE = "common_static/videos.txt"
VIDEOS_PER_BLOCK = 9
STATIC_URL = "static"
TEMPLATES_DIR = "views"
LANGS = [('en_GB', 'English'),
         ('ru_RU', 'Russian')]
DEFAULT_LOCALE = 'en'
LOCALES_DIR = "./locale/"

ALL_VIDEOS = None


env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATES_DIR),
    extensions=['jinja2.ext.i18n']
)
translations_map = {}
for l, _ in LANGS:
    lang_code = l.split("_")[0]
    t = support.Translations.load(LOCALES_DIR, [l])
    translations_map[lang_code] = t


def jinja2_view(template_name):
    def decorator(view_func):
        @functools.wraps(view_func)
        def wrapper(*args, **kwargs):
            response = view_func(*args, **kwargs)
            if isinstance(response, dict):
                lang = bottle.request.query.get('lang', DEFAULT_LOCALE)
                if lang not in translations_map:
                    lang = DEFAULT_LOCALE
                env.install_gettext_translations(translations_map[lang])
                template = env.get_or_select_template(template_name)
                return template.render(**response)
            return response
        return wrapper
    return decorator


@bottle.get("/%s/<filepath:re:.*>" % STATIC_URL)
def static(filepath):
    return bottle.static_file(filepath, root="common_static/")


def get_videos(videos_num, block, all_videos, filename=VIDEOS_FILE):
    """Retrieve videos_num videos from given block

    Returns videos_data and a flag that shows if there are any more videos
    to fetch.

    """
    if all_videos is None:
        with open(filename, 'r') as f:
            all_videos = [l.strip() for l in f.readlines() if l.strip() != ""]
    # fields are id/url/name/date
    video_data = all_videos[block * videos_num: (block + 1) * videos_num]
    more_videos = len(all_videos[(block + 1) * videos_num:]) > 0
    res = []
    for line in video_data:
        fields = line.split('|')
        if len(fields) > 0:
            video_id = fields[0].split('/')[-1]
            fields = [video_id] + fields
            res.append(fields)
    return res, more_videos


@bottle.route("/get_videos")
def get_videos_as_json():

    def _get_int(val):
        try:
            return int(val)
        except ValueError:
            return None

    query = bottle.request.query
    num = _get_int(query.n) or VIDEOS_PER_BLOCK
    block = _get_int(query.block) or 0
    videos, more = get_videos(num, block, ALL_VIDEOS)
    data = {'videos': videos, 'more_videos': 'true' if more else 'false'}
    return json.dumps(data)


@bottle.route("/")
@jinja2_view("index.html")
def index():
    videos, more = get_videos(VIDEOS_PER_BLOCK, 0, ALL_VIDEOS)
    return {"videos": videos,
            "more_videos": more,
            "static_url": STATIC_URL}


app = bottle.default_app()
app.run(host="localhost", port=8080)
