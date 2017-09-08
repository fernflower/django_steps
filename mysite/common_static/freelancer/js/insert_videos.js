var videos_block = 1;
var videos_num = 9;
var show_more_button_enabled = true;

function create_meta_elem(name, content, append_to) {
    meta = document.createElement("meta");
    meta.setAttribute("itemprop", name);
    meta.setAttribute("content", content);
    append_to.appendChild(meta);
    return meta;
}

function create_link_elem(name, href, append_to) {
    link = document.createElement("link");
    link.setAttribute("itemprop", name);
    link.setAttribute("href", href);
    append_to.appendChild(link);
    return link;
}

function do_insert(data) {
    $.each(data.videos,
           function() {
               var div = document.createElement('div');
               div.setAttribute("class", "col-sm-4 portfolio-item");
               var a = document.createElement('a');
               a.setAttribute("href", "#");
               a.setAttribute("class", "portfolio-link");
               a.setAttribute("data-toggle", "modal");
               var a_div = document.createElement('div');
               a_div.setAttribute("class", "embed-responsive embed-responsive-4by3");
               var iframe = document.createElement('iframe');
               iframe.setAttribute("class", "embed-responsive-item");
               iframe.setAttribute("allowfullscreen", "");
               iframe.setAttribute("src", this[1]);
               create_meta_elem("isFamilyFriendly", "true", a_div);
               create_meta_elem("uploadDate", this[3], a_div);
               create_meta_elem("name", this[2], a_div);
               create_meta_elem("description", this[2], a_div);
               create_meta_elem("thumbnail", "https://img.youtube.com/vi/" + this[0] + "/0.jpg", a_div);
               create_meta_elem("duration", this[4], a_div);
               create_link_elem("url", this[1], a_div);
               create_link_elem("thumbnailUrl", "https://img.youtube.com/vi/" + this[0] + "/0.jpg", a_div);
               div.appendChild(a);
               a.appendChild(a_div);
               a_div.appendChild(iframe);
               document.getElementById("videos_row").appendChild(div);
           });
    show_more_button_enabled = data.more_videos;
    if (show_more_button_enabled != "true") {
        $("#show_more_videos_btn").prop('disabled', 'disabled');
    }
}

function insert_videos(n=videos_num, block=videos_block) {
    $.getJSON("get_videos?n=" + n + "&block=" + block, function(data) {do_insert(data);});
    videos_block = videos_block + 1;
}
