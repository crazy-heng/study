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

//标题栏切换
var tabli = document.getElementsByTagName('li')
var tabContent = document.getElementsByClassName('content-list')
console.log(tabContent)
for(var i=0;i<tabli.length;i++) {
    //保存点击值存入index变量
    tabli[i].index = i;
    tabli[i].onclick = function () {
        for(var j=0;j<tabli.length;j++){
                tabContent[j].className = 'content-list'
            }
        tabContent[this.index].className = "content-list show"
    }
}
