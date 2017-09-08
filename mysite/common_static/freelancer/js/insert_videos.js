var videos_block = 1;
var videos_num = 9;
var show_more_button_enabled = true;

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
