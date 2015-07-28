// FIXME preview should be opened in a single window that is refreshed
var previewWindow = null;

function has_changes() {
    $('#apply-changes').prop('disabled', false);
}

function no_changes() {
    $('#apply-changes').prop('disabled', true);
}

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
        has_changes();
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
    $('.post-visibility').click(function(){
        has_changes();
        $(this).toggleClass('invisible-post-icon');
    });
    return false;
});

$(function() {
    $('.post-favourites').click(function(){
        has_changes();
        $(this).toggleClass('not-favourite-post');
    });
    return false;
});

function preview_changes() {
    // collect visible posts' ids
    var visible_posts = $('.row').not('.post-to-delete').find('.post-visibility')
        .not('.invisible-post-icon').siblings('.hidden-id').map(function() {
        return $(this).text();
    }).get();
    var data = JSON.stringify({'visible': visible_posts});
    var preview_url = '/posts/preview';
    $.ajax({
        url: preview_url,
        type: 'post',
        data: data,
        headers: {'X-CSRFToken': getCookie('csrftoken'),
                  'Content-Type': 'application/json;charset=utf-8'},
        success: function(result) {
                wind.document.write(result);
        }
    });
    return false;
}

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
    // collect visible posts' ids
    var visible_posts = $('.row').not('.post-to-delete').find('.post-visibility')
        .not('.invisible-post-icon').siblings('.hidden-id').map(function() {
        return $(this).text();
    }).get();
    // collect favourite posts' ids
    var favourites = $('.row').not('.post-to-delete').find('.post-favourites')
        .not('.not-favourite-post').siblings('.hidden-id').map(function() {
        return $(this).text();
    }).get();
    // collect all posts' ids to work with
    var all_posts = $('.row').not('.post-to-delete').find('.hidden-id').map(function() {
        return $(this).text();
    }).get();

    for (i = 0; i < all_posts.length; i++) {
        var post_id = all_posts[i];
        var update_url = "/posts/" + post_id + "/update";
        var is_visible = visible_posts.indexOf(post_id) > -1;
        var is_favourite = favourites.indexOf(post_id) > -1;
        var data = JSON.stringify({'is_visible': is_visible,
                                   'is_favourite': is_favourite});
        $.ajax({
            url: update_url,
            type: 'post',
            data: data,
            headers: {'X-CSRFToken': getCookie('csrftoken'),
                      'Content-Type': 'application/json;charset=utf-8'},
            success: function(result) {
                return false;
            }
        });
    }
    no_changes();
}
