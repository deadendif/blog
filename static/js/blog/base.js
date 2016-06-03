$(function(){
    $('#search-btn').on('click', function(){
        var keyword = $('#search-keyword').val();
        location.href = '/search/' + keyword + '/';
    });
});
