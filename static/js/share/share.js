
/* 模态窗初始化 */
var buildModal = function(conf) {
    if (conf['title'] != undefined) {
        $('#md-title i').addClass(conf['title']['icon'] != undefined ? conf['title']['icon'] : '');
        $('#md-title span').text(conf['title']['text'] != undefined ? conf['title']['text'] : '')
    }

    if (conf['content'] != undefined) {
        $('#md-content p').text(conf['content']);
    }

    if (conf['actions'] != undefined) {
        $.each(conf['actions'], function(key, val) {
            if (conf['actions'][key]['exists']) {
                $('#md-actions .' + key + ' span').text(conf['actions'][key]['text']);
            } else {
                $('#md-actions .' + key).remove();
            }
        });
    } else {
        $('#md-actions').remove();
    }
};

$(function(){

});