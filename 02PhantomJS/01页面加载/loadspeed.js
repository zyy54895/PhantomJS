var page = require('webpage').create(),
    system = require('system'),
    t,address;
if (system.args.length === 1) {
    console.log('Usage: loadspeed.js <some URL>');
    phantom.exit();
}
t = Date.now();
address = system.args[1];
page.open(address, function(status){
    if (status !== 'success'){
        console.log('FAIL to load the address');
    }else{
        t = Date.now() - t;
        console.log('Loading ' + system.args[1]);
        console.log('Loading time ' + t + 'msec');        
    }
    phantom.exit();
});


/*
代码解释：首先使用webpage模块创建一个page对象，使用system模块获取系统对象system，并声明了两个变量t和address，用来保存时间和传入参数。
如果传入参数的长度等于1，说明要加载的地址没有传入，进行提示并推出phantom。为什么要等于1呢？因为phantomjs loadspeed.js第一个参数是loadspeed.js。
接着获取当前的时间，然后打开网页，获取加载完成后的时间，进行相减即可。

*/