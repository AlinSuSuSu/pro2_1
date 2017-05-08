/**
 * Created by Administrator on 2017-04-04.
 */

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
                        },
                        regexp: {
                            regexp: /^[0-9]{11}$/,
                            message: '请输入11位数字'

                        }

                    }
                },
                owner_owneridcard:{
                     message:'输入不合法',
                    validators:{
                        notEmpty:{
                            message:'身份证号不能为空'
                        },
                        stringLength:{
                            max:18,
                            min:18,
                            message:"请输入11位"
                        },
                        regexp:{
                            regexp:/^[0-9]{17}[0-9|x]$/,
                            message:'输入不合法'

                        }

                    }
                },
                owner_owneryears:{
                    message:'输入不合法',
                    validators: {
                        notEmpty:{
                             message:'不能为空'
                        },

                        stringLength: {
                            min: 1,
                            max: 3,
                            message: '不能超过3位数'
                        },
                        regexp: {
                            regexp: /^[0-9]{1,3}$/,
                            message: '最多两位整数'

                        }

                    }
                },



            }
        });



         //提交后页面跳转
        $("#house_validateBtn").on("click", function(){
            var bootstrapValidator = $("#houseForm").data('bootstrapValidator');
            bootstrapValidator.validate();
            if(bootstrapValidator.isValid()) {
                document.getElementById("houseForm").submit(function(ev){ev.preventDefault();});

            }
            else return;
        });

        $('#houseForm').bootstrapValidator({
            message:'输入不合法',
            feedbackIcons: {
                    valid: 'glyphicon glyphicon-ok',
                    invalid: 'glyphicon glyphicon-remove',
                    validating: 'glyphicon glyphicon-refresh'
                },
            fields: {
                add_housespace: {
                    message:'输入不合法',
                    validators: {
                        notEmpty: {
                            message:'不能为空'
                        },
                        stringLength:{
                            min:2,
                            max:3,
                            message:'不能大于1000'
                        },
                        regexp:{
                            regexp:/^[1-9]{1,3}.?[1-9]{1,2}$/,
                            message:'最多两位小数，且不得超过1000'

                        }


                    }
                },
                add_housetype:{
                     message:'输入不合法',
                    validators: {
                        notEmpty: {
                            message: '不能为空'
                        },
                        stringLength: {
                            min: 7,
                            max: 11,
                            message:"输入不合法"
                        },
                        regexp: {
                            regexp: /^[1-9]{1,2}\/[0-9]?\/[0-9]?\/[0-9]?$/,
                            message:"输入不合法"

                        }

                    }
                },
                add_houseyears:{
                     message:'输入不合法',
                    validators: {
                        stringLength: {
                            min: 1,
                            max: 3,
                            message: '不能超过3位数'
                        },
                        regexp: {
                            regexp: /^[0-9]{1,3}$/,
                            message: '最多两位整数'

                        }

                    }
                },
                add_housecommunity: {
                    message: '输入不合法',
                    validators: {
                        notEmpty: {
                            message: '不能为空'

                        },
                        stringLength: {
                            min: 1,
                            max: 20,
                            message: '不能超过20个字符'
                        },
                    },
                },
                add_houseaddress:{
                    message:"输入不合法",
                    validators:{
                        notEmpty:{
                            message:'不能为空'

                        },
                        stringLength: {
                            min: 1,
                            max: 128,
                            message: '不能超过128个字符'
                        },


                    },

                },
                add_houseid:{
                    message:'输入不合法',
                    validators:{
                        notEmpty:{
                            message:'不能为空'

                        },
                        stringLength: {
                            min: 10,
                            max: 10,
                            message: '必须为10位'
                        },
                        regexp: {
                            regexp: /^[0-9]{10}$/,
                            message: '10位整数'
                        }

                    }

                },

                add_houseremark:{
                    message:"输入不合法",
                    validators:{
                         stringLength:{
                            max:1,
                            min:64,
                            message:"不能超过64位"
                        }
                    }
                }


            }
        });

        $('#housedetailForm').bootstrapValidator({
            message:'输入不合法',
            feedbackIcons: {
                    valid: 'glyphicon glyphicon-ok',
                    invalid: 'glyphicon glyphicon-remove',
                    validating: 'glyphicon glyphicon-refresh'
                },
            fields: {
                detail_housespace: {
                    message:'输入不合法',
                    validators: {
                        notEmpty: {
                            message:'不能为空'
                        },
                        stringLength:{
                            min:2,
                            max:3,
                            message:'不能大于1000'
                        },
                        regexp:{
                            regexp:/^[1-9]{1,3}.?[1-9]{1,2}$/,
                            message:'最多两位小数，且不得超过1000'

                        }


                    }
                },
                detail_housetype:{
                     message:'输入不合法',
                    validators: {
                        notEmpty: {
                            message: '不能为空'
                        },
                        stringLength: {
                            min: 7,
                            max: 11,
                            message:"输入不合法"
                        },
                        regexp: {
                            regexp: /^[1-9]{1,2}\/[0-9]?\/[0-9]?\/[0-9]?$/,
                            message:"输入不合法"

                        }

                    }
                },
                detail_houseyears:{
                     message:'输入不合法',
                    validators: {
                        stringLength: {
                            min: 1,
                            max: 3,
                            message: '不能超过3位数'
                        },
                        regexp: {
                            regexp: /^[0-9]{1,3}$/,
                            message: '最多两位整数'

                        }

                    }
                },
                detail_housecommunity: {
                    message: '输入不合法',
                    validators: {
                        notEmpty: {
                            message: '不能为空'

                        },
                        stringLength: {
                            min: 1,
                            max: 20,
                            message: '不能超过20个字符'
                        },
                    },
                },
                detail_houseaddress:{
                    message:"输入不合法",
                    validators:{
                        notEmpty:{
                            message:'不能为空'

                        },
                        stringLength: {
                            min: 1,
                            max: 128,
                            message: '不能超过128个字符'
                        },


                    },

                },

                detail_houseremark:{
                    message:"输入不合法",
                    validators:{
                         stringLength:{
                            max:1,
                            min:64,
                            message:"不能超过64位"
                        }
                    }
                }


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

        /*$('#owner_add_validateBtn').click(function() {
            $('#ownerForm').bootstrapValidator('validate');
        });*/
        $('#owner_add_resetBtn').click(function() {
            $('#ownerForm').data('bootstrapValidator').resetForm(true);
        });


    });


