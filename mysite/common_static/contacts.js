$(function() {
    $('.captcha-refresh').click(function(){
        console.log('123');
        var $form = $('form');
        var url = '/captcha/refresh';
        $.getJSON(url, {}, function(json) {
            $form.find('input[name="captcha_0"]').val(json.key);
            $form.find('img.captcha').attr('src', json.image_url);
        });

        return false;
    });
});
