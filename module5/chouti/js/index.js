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
        console.log("login")
    })

})
//注册
$(function () {
    $('.reg').click(function () {
        console.log("reg")
    })

})
