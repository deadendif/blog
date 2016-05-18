$(function(){
    $('.about.menu .item').tab({history:false});
    $('.ui.form')
        .form({
            on: 'blur',
            fields: {
                'address': {
                    identifier: 'address',
                    rules: [
                        {
                            type   : 'email',
                            prompt : 'Please enter a valid e-mail'
                        }
                    ]
                },
                'name': {
                    identifier: 'name',
                    rules: [
                        {
                            type   : 'empty',
                            prompt : 'Please enter your name'
                        }
                    ]
                },
                'topic': {
                    identifier: 'topic',
                    rules: [
                        {
                            type: 'empty',
                            prompt: 'Please enter the topic'
                        },
                        {
                            type: 'minLength[6]',
                            prompt: 'The topic is too short. Please enter again'
                        }
                    ]
                },
                'content': {
                    identifier: 'content',
                    rules: [
                        {
                            type: 'empty',
                            prompt: 'Please enter the content'
                        },
                        {
                            type: 'minLength[20]',
                            prompt: 'The content is too short. Please enter again'
                        }
                    ]
                }
            }
        })
        .submit(function(event){
            event.preventDefault();
            var datas = {};
            $.each($(this).serializeArray(), function(i, val){
                datas[val.name] = val.value;
            });
            $.ajax({
                type: 'POST',
                url: './',
                data: datas,
                dataType: 'json',
                success: function(data){
                    if (data[0]['status'] == 0) {
                        
                    }
                }
            });
        });

});