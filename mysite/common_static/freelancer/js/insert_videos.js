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
}

function insert_videos(n=9, block=0) {
    $.getJSON("get_videos?n=" + n + "&block=" + block, function(data) {do_insert(data); });
}
