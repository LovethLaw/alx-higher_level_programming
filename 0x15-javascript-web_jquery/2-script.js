#!/usr/bin/node

$(document).ready(() => {
  $('DIV#red_header').click(function () {
    $('header').css('color', 'red');
  });
});
