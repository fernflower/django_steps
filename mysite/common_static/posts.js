//a func to retrieve csrf token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(function() {
    $('.delete-post-icon').click(function(){
        if ($(this).parent().hasClass('post-to-delete')) {
            $(this).parent().removeClass('post-to-delete');
        }
        else {
            $(this).parent().addClass('post-to-delete');
        }
        return false;
    });
});

function get_selected_scraped() {
    var post_ids = $(".post-to-delete").find('.hidden-id').map(function() {
        return $(this).text();
    }).get();
    return post_ids;
}

function delete_selected_scraped() {
    var post_ids = $(".post-to-delete").find('.hidden-id').map(function() {
        return $(this).text();
    }).get();

    var csrftoken = getCookie('csrftoken');
    // TODO 
    // do not violate DRY principle, try to use url template tag reference! 
    var delete_url = "/posts/delete";
    var data = {'ids': post_ids}
    $.ajax({
        url: delete_url,
        type: 'post',
        data: {'ids': post_ids},
        headers: {'X-CSRFToken': getCookie('csrftoken')},
        success: function(result) {
            $(".post-to-delete").css("display", "none");
        }
    });
}
