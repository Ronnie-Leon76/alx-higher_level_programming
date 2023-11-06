$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val();
    console.log(url)
    $.getJSON(url, function (data) {
        console.log(data);
      $('DIV#hello').text(data.hello);
    });
  });
});
