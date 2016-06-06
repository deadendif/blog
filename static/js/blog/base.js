$(function(){
    /* 代码高亮 */
    hljs.initHighlightingOnLoad();

    /* 搜索 */
    $('#search-btn').on('click', function(){
        var keyword = $('#search-keyword').val();
        location.href = '/search/' + keyword + '/';
    });
});
