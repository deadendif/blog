$(function(){
    $('#search-btn').on('click', function(){
        var keyword = $('#search-keyword').val();
        location.href = '/blog/search/' + keyword + '/';
    });
});