//置顶按钮显现
$(function () {
        var h = $('.head-band').height()
        $(document).scroll(function () {
            var scollTop = $(document).scrollTop()
            if(h<scollTop){
                 $('.gotop').css({display:'block'})
            }else{
                $('.gotop').css({display:'none'})
            }
        })

    })
