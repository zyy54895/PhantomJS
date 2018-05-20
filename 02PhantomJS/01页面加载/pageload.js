var page = require('webpage').create();
page.open('http://www.cnblogs.com/qiyeboy/', function(status){
	console.log("Status:" + status);
	if (status==="success"){
		page.render('qiye.pdf');
	}
	phantom.exit();
});

/*
代码解释：首先使用webpage模块创建一个page对象，然后通过page对象打开http://www.cnblogs.com/qiyeboy/网址，
如果请求相应状态为success，则通过render方法将当前页面保存为qiye.png图片。

*/