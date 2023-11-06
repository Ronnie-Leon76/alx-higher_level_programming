$(document).ready(function () {
    $('INPUT#btn_translate, INPUT#language_code').click(function () {
        const url = 'https://fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val();
        $.getJSON(url, function (data) {
            $('DIV#hello').text(data.hello);
        });
    });
});