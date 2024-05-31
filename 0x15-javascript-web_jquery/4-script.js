#!/usr/bin/node

$(document).ready(() => {
  $('DIV#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
