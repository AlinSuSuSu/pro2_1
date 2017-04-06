/**
 * Created by Administrator on 2017-04-04.
 */

    window.onload=function(){
        $("#addhouseid").focus()
    }

    /*失焦判断**/
    $("input").blur(function(){
        $(".ss-house-span").css("color","#BD362F")
        if($(this).is("#addhouseid")){
            var houseid=/^[0-9]{10}$/
            if($("#addhouseid").val()!=''){
                if(!(houseid.test($('#addhouseid').val()))){
                    $(".ss-house-span1").text('请输入10位数字');
                    $(this).css("border","1px solid #BD362F")
                    return false;
                }else if(houseid){
                    $(".ss-house-span1").text("");
                    $(this).css("border","1px solid #ccc")

                    return true;
                }
            }else{
                $(".ss-house-span1").text("");
                $(this).css("border","1px solid #ccc")

            }
        }
        if($(this).is("#addhousespace")) {
            var housespace = /^[0-9]{1,}.?[0-9]{2}/
            if ($("#addhousespace").val() != '') {
                if (!(housespace.test($('#addhousespace').val()))) {
                    $(".ss-house-span2").text('精确到小数点后两位')
                    $(this).css("border", "1px solid #BD362F")
                    return false;
                } else if (housespace) {
                    $(".ss-house-span2").text("");
                    $(this).css("border", "1px solid #ccc")
                    return true;
                }
            }else {
                $(".ss-house-span2").text("");
                $(this).css("border", "1px solid #ccc")
            }
        }

        var atype=["#addhousetype1","#addhousetype2","#addhousetype3","#addhousetype4"]

        /*if($(this).is(atype[i])) {
            //var i=Math.round(Math.random()*3+1);
            var housetype = /^[0-5]$/
            if ($("#addhousetype1").val() != '') {
                if (!(housetype.test($("#addhousetype1").val()))) {
                    $(".ss-house-span3").text('一位整数')
                    $(this).css("border", "1px solid #BD362F")
                    return false;
                } else if (housetype) {
                    $(".ss-house-span3").text("");
                    $(this).css("border", "1px solid #ccc")
                    return true;
                }
            }else {
                $(".ss-house-span3").text("");
                $(this).css("border", "1px solid #ccc")
            }

        }*/
    })

    /**聚焦判断**/
    /*
    $("input").focus(function(){
        if($(this).is("#addhouseid")){
            $(".ss-house-span1".text("10个数字").css("color","#aaa"))
            $(this.css("border","1px solid #aaa"))
        }
    })*/

