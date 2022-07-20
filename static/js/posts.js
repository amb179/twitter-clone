/////////////////////////////
/// javascript for posts page
/////////////////////////////


$(function () {
    // executed when js-menu-icon is clicked
    $('.js-menu-icon').click(function () {
        // $(this) : self elemt, namely div.js-menu-icon
        // next() : next to div.js-menu-icon, namely div.menu
        // toggle() : switch show and hide
        $(this).next().toggle(); 
    })
})

