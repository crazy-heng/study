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
//发布
$(function () {
    $('.publish-btn').click(function () {
        $('.publish').css({display:'block'})
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
$(function () {
    $('.pub-close').click(function () {
        $('.publish').css({display:'none'})
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

//确认发布
$(function () {
    $('.pub-confirm').click(function () {
        var todolist = document.getElementById("content-list")
        var stringOld = todolist.innerHTML
        var title = $('#title').val()
        var content = $('#inputContent').val()
        var url = $('#url').val()
        console.log(title)
        console.log(content)
        console.log(url)
        if(title == undefined || content == undefined || url == undefined){ // "",null,undefined
            alert("输入有误！");
        }else {
            var stringNew = "<div class=\"media\">\n" +
                "                          <div class=\"media-body\">\n" +
                "                              <h4 class=\"media-heading\">" + title + "</h4>\n" +
                "                              <p class=\"content\">" + content + "</p>\n" +
                "                          </div>\n" +
                "                          <div class=\"media-right\">\n" +
                "                              <a href=\"#\">\n" +
                "                              <img class=\"media-object\" src=\"" + url + "\" alt=\"...\">\n" +
                "                              </a>\n" +
                "                          </div>\n" +
                "                          <div class=\"media-bottom\">\n" +
                "                              <a href=\"#\">点赞 <span class=\"badge\">0</span></a>\n" +
                "                              <a href=\"#\">评论 <span class=\"badge\">0</span></a>\n" +
                "                          </div>\n" +
                "                      </div>"
            var todoString = stringNew + stringOld
            todolist.innerHTML = todoString
            console.log(todolist)
            console.log(todoString)
            document.getElementById("title").value=""
            document.getElementById("inputContent").value=""
            document.getElementById("url").value=""
        }
        $('.publish').css({display:'none'})
    })
})

//点赞
