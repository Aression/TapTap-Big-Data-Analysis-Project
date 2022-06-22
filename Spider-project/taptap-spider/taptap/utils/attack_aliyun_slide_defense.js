function RandomNumBoth(Min,Max){
      var Range = Max - Min;
      var Rand = Math.random();
      var num = Min + (Rand * Range);
      return num;
}

function slide (id) {
    var slider    = document.getElementById(id),
        container = slider.parentNode;

    var rect = slider.getBoundingClientRect(),
        x0          = rect.x || rect.left,
        y0          = rect.y || rect.top,
        w           = container.getBoundingClientRect().width;

    var mousedown = document.createEvent("MouseEvents");
    mousedown.initMouseEvent("mousedown", true, true, window, 0,
        x0, y0, x0, y0, false, false, false, false, 0, null);
    slider.dispatchEvent(mousedown);

    dx = 0;
    dy = 0;
    //»¬¶¯»¬¿é
    intervaltimer = setInterval(function(){
        var mousemove = document.createEvent("MouseEvents");
        var _x = x0 + dx;
        var _y = y0 + dy;
        mousemove.initMouseEvent("mousemove",true,true,window,0,
                _x, _y, _x, _y,false,false,false,false,0,null);

        slider.dispatchEvent(mousemove);
        if(_x - x0 >= w){
            clearInterval(intervaltimer);
            var mouseup = document.createEvent("MouseEvents");
            mouseup.initMouseEvent("mouseup",true,true,window,0,
            _x, _y, _x, _y,false,false,false,false,0,null);
            slider.dispatchEvent(mouseup);
            setTimeout(function(){
                console.log('ÍÏ¶¯½áÊøÖ´ĞĞÂß¼­');
            }, 1000);
        }
        else{
            dx += RandomNumBoth(-5,15);
            dy = RandomNumBoth(dy-1,dy+1);
            console.log(x0,y0,_x,_y,dx);
        }
    }, 30);
}
slide('nc_1_n1z');