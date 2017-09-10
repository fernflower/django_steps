import bottle
import json

VIDEOS_FILE = "common_static/videos.txt"
VIDEOS_PER_BLOCK = 9
STATIC_URL = "static"

ALL_VIDEOS = None


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
def index():
    videos, more = get_videos(VIDEOS_PER_BLOCK, 0, ALL_VIDEOS)
    return bottle.template("index", videos=videos, more_videos=more,
                           static_url=STATIC_URL)


bottle.run(host="localhost", port=8080)
