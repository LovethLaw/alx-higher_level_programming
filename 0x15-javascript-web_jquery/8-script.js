#!/usr/bin/node

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$(document).ready(() => {
  $.get(url, function (body) {
    $.each(body.results, function (index, item) {
      $('UL#list_movies').append(`<li>${item.title}</li>`);
    });
  });
});
