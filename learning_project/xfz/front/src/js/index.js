//先创建一个面向对象类，可以方便动态增加类的属性和方法
function Banner(){
    this.bannerGroup = $(".banner-group");
    this.index = 0;//将index放到构造函数里，这样才能做为全局变量
    //对象初始化后，就执行监听hover事件
    this.listenBannerHover();
};
//监听banner-group 的hovers事件
Banner.prototype.listenBannerHover = function(){
    var self = this;
    console.log('进入监听里面')
    this.bannerGroup.hover(function(){
        //第一个函数：把鼠标移动到banner上会执行的函数
        // clearInterval(this.timer)这里不能直接用this，因为这个this代表的是function，不是Banner类
        console.log('hover激活')
        clearInterval(self.timer)
    },function(){
        //第二个函数: 把属性移走会重新调用定时器
        self.loop();
    });
} 

Banner.prototype.loop = function(){
    console.log(this)
    var self = this;
    var bannerUI = $("#banner-UI");
    // setInterval定时器，2000，代表定时器里的函数执行的间隔是2000ms
    //this是为了将timer这个方法也赋给Banner这个类，方便上面调用
    this.timer = setInterval(function(){
            if(self.index >= 3){
                self.index = 0;
            }else{
                self.index ++;
            }
            // 下面是轮播动画，500代表动画执行500ms
            console.log(self.index)
            bannerUI.animate({"left":-795*self.index},500);
        },2000)
}

// prototype是原型链，为了给Banner类赋予一个run方法，
Banner.prototype.run = function(){
    this.loop()
}


//$符号是jquery特有的，表示$函数中的函数function是要在所有html文档加载完之后才会执行
$(function(){
    var banner = new Banner();
    banner.run();
});