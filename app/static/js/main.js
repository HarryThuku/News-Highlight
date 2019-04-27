$(window).scroll(()=>{
    if ($().scrollTop()>50){
        $('nav').addClass('shrink');
    } else {
        $('nav').removeClass('shrink');
    };
});