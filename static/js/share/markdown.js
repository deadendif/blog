/* Markdown */
$(function(){
    /* table style */
    $('.markdown-body table').addClass('ui yellow striped table');

    /* link target */
    $('.markdown-body a').attr('target', '_blank');
    $('.markdown-body h3 a').attr('target', '_self');
});
