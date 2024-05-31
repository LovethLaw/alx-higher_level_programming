#!/usr/bin/node
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$(document).ready(() => {
  $.get(url, function (body) {
    $('DIV#hello').text(body.hello)
  });
});