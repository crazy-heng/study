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
//登录
$(function () {
    $('.login').click(function () {
        $('.login-m').css({display:'block'})
    })

})
//注册
$(function () {
    $('.reg').click(function () {
        $('.reg-m').css({display:'block'})
    })
})
$(function () {
    $('.login-close').click(function () {
        $('.login-m').css({display:'none'})
    })
})
$(function () {
    $('.reg-close').click(function () {
        $('.reg-m').css({display:'none'})
    })
})
