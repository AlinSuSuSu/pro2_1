/**
 * Created by Administrator on 2017-04-04.
 */
/**
     window.onload=function(){
        $("#addhouseid").focus()
    }

    /*失焦判断
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


        //var atype=["#addhousetype1","#addhousetype2","#addhousetype3","#addhousetype4"]

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

        }
    })
    $("select").blur(function() {
     if ($(this).is("#addhouse_houseid")) {
         var housespace = /^[0-9]{1,}.?[0-9]{2}/
         if ($("#addhouse_houseid").val() == '' || $("#addhouse_houseid").val() == None) {
             $(".ss-owner-span2").text('房屋编号不能为空')
             $(this).css("border", "1px solid #BD362F")
             return false;

         }
     }
    })
    /**聚焦判断**/
    /*
    $("input").focus(function(){
        if($(this).is("#addhouseid")){
            $(".ss-house-span1".text("10个数字").css("color","#aaa"))
            $(this.css("border","1px solid #aaa"))
        }
    })*/
    /*
    $("#owner_submit").click(function(){
            if($("#addhouse_houseid").val()=="" || $("#addhouse_houseid").val() == None){
                $(".ss-owner-span2").text('请选择房屋编号')
                $(this).css("border", "1px solid #BD362F")
                return false;
            }

    })*/


    $(document).ready(function() {

        $("#owner_add_validateBtn").on("click", function(){
            var bootstrapValidator = $("#ownerForm").data('bootstrapValidator');
            bootstrapValidator.validate();
            if(bootstrapValidator.isValid()) {
                document.getElementById("ownerForm").submit(function(ev){ev.preventDefault();});

            }
            else return;
        });
        $('#ownerForm').bootstrapValidator({
            message:'输入不合法',
            feedbackIcons: {
                    valid: 'glyphicon glyphicon-ok',
                    invalid: 'glyphicon glyphicon-remove',
                    validating: 'glyphicon glyphicon-refresh'
                },
            fields: {
                owner_ownername: {
                    message:'用户名不合法',
                    validators: {
                        notEmpty: {
                            message:'用户名不能为空'
                        },
                        stringLength:{
                            min:2,
                            max:16,
                            message:'用户名至少两个字符'
                        }

                    }
                },
                owner_houseid:{
                    message:'输入不合法',
                    validators:{
                        notEmpty:{
                            message:'编号不能为空'
                        }

                    }

                },
                owner_ownerphone:{
                    message:'输入不合法',
                    validators:{
                        notEmpty:{
                            message:'手机号不能为空'
                        },
                        stringLength:{
                            max:11,
                            min:11,
                            message:"请输入11位"
                        }

                    }
                },

            }
        });

        $('#patrol_validateBtn').click(function() {
            $('#patrolForm').bootstrapValidator("validate")
        });
        $('#patrol_resetBtn').click(function() {
            $('#patrolForm').data('bootstrapValidator').resetForm(true);
        });
        $('#house_validateBtn').click(function() {
            $('#houseForm').bootstrapValidator('validate');
        });
        $('#house_resetBtn').click(function() {
            $('#houseForm').data('bootstrapValidator').resetForm(true);
        });
        $('#house_detail_validateBtn').click(function() {
            $('#housedetailForm').bootstrapValidator('validate');
        });

        $('#choice_patrol_validateBtn').click(function() {
            $('#choicepatrolForm').bootstrapValidator('validate');
        });
        $('#choice_infrastructure_validateBtn').click(function() {
            $('#choiceinfrastructureForm').bootstrapValidator('validate');
        });
        $('#house_detail_resetBtn').click(function() {
            $('#housedetailForm').data('bootstrapValidator').resetForm(true);
        });
        /*$('#owner_add_validateBtn').click(function() {
            $('#ownerForm').bootstrapValidator('validate');
        });*/
        $('#owner_add_resetBtn').click(function() {
            $('#ownerForm').data('bootstrapValidator').resetForm(true);
        });

    });


