#!/usr/bin/node
const url = "https://swapi-api.alx-tools.com/api/people/5/?format=json"
$(document).ready(()=>{
    $.get(url, function(body, status){
        if (status == 'success'){
            $('DIV#character').text(body.name);
        }
    });
});