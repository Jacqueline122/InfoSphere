function bindEmailCaptchaClick(){
     $("#captcha-btn").click(function (event) {
        // jquery object
        var $this = $(this);
        event.preventDefault();

        var email = $("input[name='email']").val();
        $.ajax({
            url:"/auth/captcha/email?email="+email,
            method: "GET",
            success:function (result) {
                var code = result['code'];
                if (code === 200){
                    var countdown = 5;
                    // make the button unclickable
                    $this.off("click")
                    var timer = setInterval(function () {
                        $this.text(countdown);
                        countdown -= 1;
                        // after the timer is done
                        if (countdown <= 0){
                            // clear the timer
                            clearInterval(timer);
                            $this.text("Get Code");
                            bindEmailCaptchaClick();
                        }

                    }, 1000);
                    // alert("sent successfully");
                }else{
                    alert(result['message']);
                }
            },
            fail: function (error) {
                console.log(error);
            }

        })
    });
}

// after the website is loaded
$(function(){
    bindEmailCaptchaClick()
})