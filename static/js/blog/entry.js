
/* 恢复全屏状态 */
var restoreFullscreen = function() {
    var isFullscreen = Cookies.get('isFullscreen');
    if (isFullscreen == 'true') {
        $('#body-right').hide();
        $('#fullscreen').attr("checked",'true');
        $('#body-left').removeClass('eleven wide column').addClass('sixteen wide column');
    }
};


/* 切换全屏状态 */
var toggleFullscreen = function(setCookie) {
    var isFullscreen = Cookies.get('isFullscreen');
    if (isFullscreen == undefined || isFullscreen == 'false') {
        $('#body-right').hide();
        $('#body-left').removeClass('eleven wide column').addClass('sixteen wide column');
        if (setCookie)
            Cookies.set('isFullscreen', 'true');
    } else {
        $('#body-right').show();
        $('#body-left').removeClass('sixteen wide column').addClass('eleven wide column');
        if (setCookie)
            Cookies.set('isFullscreen', 'false');
    }
};


/* 监听滚动状态切换全屏状态 */
var toggleFullscreenWhenScroll = function() {
    var isFullscreen = Cookies.get('isFullscreen');
    if (isFullscreen != 'true') {
        var toTop = $(document).scrollTop();
        if (toTop > $('#landmark-scroll').offset().top * 2 / 3) {
            if ($('#body-left').hasClass('eleven wide column')) {
                $('#body-right').hide();
                $('#body-left').removeClass('eleven wide column').addClass('sixteen wide column');
            }
        } else {
            if ($('#body-left').hasClass('sixteen wide column')) {
                $('#body-right').show();
                $('#body-left').removeClass('sixteen wide column').addClass('eleven wide column');
            }
        }
    }
};


/* 反馈 useful or useless */
var feedback = function(btn, type) {
    $.ajax({
        type: 'POST',
        url: './',
        data: {'type': type},
        dataType: 'json',
        success: function(data) {
            if (data[0]['status'] == 0) {
                var id = btn.attr('id').replace('btn', 'num');
                var before = parseInt($($('.' + id)[0]).text());
                $('.' + id).text(before + 1);
            } else {
                var feedbackConf = {
                    'title': {'icon': 'lightning', 'text': 'Attention Please'},
                    'content': data[0]['msg'],
                    'actions': {
                        'no' : {
                            'exists': false
                        },
                        'yes': {
                            'exists': true,
                            'text': 'Got it'
                        }
                    }
                };
                buildModal(feedbackConf);
                $('.basic.zzc.modal')
                  .modal('setting', 'closable', false)
                  .modal('setting', 'duration', 200)
                  .modal('show')
                ;
            }
        }
    });
};

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
}


/* 加载完成时执行 */
$(function(){
    /* 代码高亮 */
    hljs.initHighlightingOnLoad();

    /* 恢复全屏状态 */
    restoreFullscreen();

    /* 监听全屏按钮 */
    $('#fullscreen').change(function(){ toggleFullscreen(true); });

    /* 监听滚动 */
    $(window).scroll(toggleFullscreenWhenScroll);

    /* 监听反馈按钮 */
    $('#useful-btn').on('click', function(){
        feedback($(this), 1);
    });
    $('#useless-btn').on('click', function(){
        feedback($(this), -1);
    });
});