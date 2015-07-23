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

$(function() {
    $('.visible-post-icon').click(function(){
        $(this).parent().find('.invisible-post-icon').css('display', 'inline');
        $(this).css('display', 'none');
        return false;
    });
    $('.invisible-post-icon').click(function(){
        $(this).parent().find('.visible-post-icon').css('display', 'inline');
        $(this).css('display', 'none');
        return false;
    });
});

function save_changes_scraped() {
    // collect post ids to delete
    var post_ids = $(".post-to-delete:visible").find('.hidden-id').map(function() {
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
            // hide already deleted posts
            $(".post-to-delete").css("display", "none");
        }
    });
    // change visibility of a post according to visible flag
    // posts are invisible by default, so collect all visible posts
    visible_posts = $('.row').not('.post-to-delete').find('.visible-post-icon:visible')
        .siblings('.hidden-id').map(function() {
        return $(this).text();
    }).get();
    for (i = 0; i < visible_posts.length; i++) {
        var update_url = "/posts/" + visible_posts[i] + "/update";
        $.ajax({
            url: update_url,
            type: 'post',
            data: {'is_visible': true},
            headers: {'X-CSRFToken': getCookie('csrftoken')},
            success: function(result) {
                return false;
            }
        });
    }
}
