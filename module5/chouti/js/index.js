zan()
//置顶按钮显现
$(function () {
        var h = $('.head-band').height()
        $(document).scroll(function () {
            var scollTop = $(document).scrollTop()
            if(h<scollTop){
                 $('.gotop').show()
            }else{
                $('.gotop').hide()
            }
        })

    })
//登录
$(function () {
    $('.login').click(function () {
        // $('.login-m').css({display:'block'})
        $('.login-m').show()
    })

})
//注册
$(function () {
    $('.reg').click(function () {
        $('.reg-m').show()
    })
})
//发布
$(function () {
    $('.publish-btn').click(function () {
        $('.publish').show()
    })
})

$(function () {
    $('.login-close').click(function () {
        $('.login-m').hide()
    })
})
$(function () {
    $('.reg-close').click(function () {
        $('.reg-m').hide()
    })
})
$(function () {
    $('.pub-close').click(function () {
        $('.publish').hide()
    })
})

//标题栏切换
var tabli = document.getElementsByTagName('li')
var tabContent = document.getElementsByClassName('content-list')
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
        if(title == "" || content == "" || url == ""){ // "",null,undefined
            alert("输入有误,发布不能为空！");
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
                "                              <a href=\"#\" class=\"likes\">点赞 <span class=\"badge likeNums\">0</span></a>&emsp;\n" +
                "                              <a href=\"#\" class=\"comment\">评论 <span class=\"badge commentNums\">0</span></a>\n" +
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
        $('.publish').hide()
        zan()
    })
})

//点赞
function zan() {
    var like = document.getElementsByClassName('likes')
    var comment = document.getElementsByClassName('likeNums')
    console.log(like)
    console.log(comment)
    for (var i = 0; i < like.length; i++) {
        //保存点击值存入index变量
        like[i].index = i;
        like[i].onclick = function () {
            var y = comment[this.index].innerHTML
            var z = parseInt(y)
            z += 1
            comment[this.index].innerHTML = z
        }
    }
}
