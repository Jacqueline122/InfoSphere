// after the website is loaded
$(function(){
    $("#captcha-btn").click(function (event) {
        event.preventDefault();

        var email = $("input[name='email']").val();
        $.ajax({
            url:"/auth/captcha/email?email="+email,
            method: "GET",
            success:function (result) {
                var code = result['code'];
                if (code === 200){
                    alert("sent successfully");
                }else{
                    alert(result['message']);
                }
            },
            fail: function (error) {
                console.log(error);
            }

        })
    });
})