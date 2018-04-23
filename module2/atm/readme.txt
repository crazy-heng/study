目录结构：
bank：银行接口，前后台程序所在位置。
logs：记录全部的日志存放
mall：商城登录程序

bank： main.py 银行用户中心主程序，用户登录操作记录行为日志action.log
       用户操作金额流水日志 bank.log
       back.py 银行后台简易管理程序，back.log记录操作日志  用户名admin 密码 admin
       b_pay.py 商城消费扣款接口
mall:  main.py 用户登录商城消费，记录cart.log

mall测试用户：fan 密码：123  用户：cai 密码：123
用户购物历史购物记录存放mall/userdata下对应txt文件
bank测试账户：fan 密码：123  用户：cai 密码：123
用户信息存放bank/userdata下对应log文件