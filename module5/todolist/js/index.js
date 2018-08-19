//清空历史表单数据
function clear(){
	localStorage.clear();
	load();
}

//取添加的数据到表单
function postaction(){
	var title = document.getElementById("title");
	// console.log(title.value)
	if(title.value == "") {
		alert("11");
	}else{
		var data=loadData();
		console.log(data)
		var todo={"title":title.value,"done":false};
		console.log(todo)
		data.push(todo);
		saveData(data);
		var form=document.getElementById("form");
		form.reset();
		load();
	}
}

//读取本地的表单数据
function loadData(){
	var collection=localStorage.getItem("todo");
	if(collection!=null){
		return JSON.parse(collection);
	}
	else return [];
}

//存取数据到本地表单
function saveData(data){
	localStorage.setItem("todo",JSON.stringify(data));
}

//加载表单到页面根据done的值分为进行和完成并统计数值写入span标签
function load() {
    var todolist = document.getElementById("todolist");
    var donelist = document.getElementById("donelist");
    var collection = localStorage.getItem("todo");
    if (collection != null) {
        var data = JSON.parse(collection);
        var todoCount = 0;
        var doneCount = 0;
        var todoString = "";
        var doneString = "";
        for (var i = data.length - 1; i >= 0; i--) {
            //判断数据表里done初始值为false，加入到进行列表。
            if (data[i].done) {
                doneString += "<li draggable='true'><input type='checkbox' onchange='update(" + i + ",\"done\",false)' checked='checked' />"
                    + "<p id='p-" + i + "' onclick='edit(" + i + ")'>" + data[i].title + "</p>"
                    + "<a href='javascript:remove(" + i + ")'>-</a></li>";
                doneCount++;
            }
            else {
                todoString += "<li draggable='true'><input type='checkbox' onchange='update(" + i + ",\"done\",true)' />"
                    + "<p id='p-" + i + "' onclick='edit(" + i + ")'>" + data[i].title + "</p>"
                    + "<a href='javascript:remove(" + i + ")'>-</a></li>";
                todoCount++;
            }
        }
        ;
        todocount.innerHTML = todoCount;
        todolist.innerHTML = todoString;
        donecount.innerHTML = doneCount;
        donelist.innerHTML = doneString;
    }
    else {
        todocount.innerHTML = 0;
        todolist.innerHTML = "";
        donecount.innerHTML = 0;
        donelist.innerHTML = "";
    }
}

//删除数据表里的第i个元素并保存重新加载数据
function remove(i){
	var data=loadData();
	var todo=data.splice(i,1);
	saveData(data);
	load();
}

//用来处理input标签和p标签的修改并把更新的值存入数据表单
function update(i,field,value){
	var data = loadData();
	var todo = data.splice(i,1)[0];
	//更改title或done的值为修改的数据
	todo[field] = value;
	//将更新的数据插入到数据表
	data.splice(i,0,todo);
	saveData(data);
	load();
}

//处理输入数据的修改操作，并把修改后的数据传给update函数做更新
function edit(i)
{
	load();
	var p = document.getElementById("p-"+i);
	title = p.innerHTML;
	p.innerHTML="<input id='input-"+i+"' value='"+title+"' />";
	console.log(p.innerHTML)
	var input = document.getElementById("input-"+i);
	input.setSelectionRange(0,input.value.length);
	//定位数据框位置
	input.focus();
	//鼠标移出input点击后确认修改
	input.onblur = function(){
		if(input.value.length == 0){
			p.innerHTML = title;
			alert("数据不能为空！");
		}
		else{
			update(i,"title",input.value);
		}
	};
}