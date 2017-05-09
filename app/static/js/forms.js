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
        $("#patrol_validateBtn").on("click", function(){
            var bootstrapValidator = $("#patrolForm").data('bootstrapValidator');
            bootstrapValidator.validate();
            if(bootstrapValidator.isValid()) {
                document.getElementById("patrolForm").submit(function(ev){ev.preventDefault();});

            }
            else return;
        });
        $("#waterfee_validateBtn").on("click", function(){
            var bootstrapValidator = $("#waterfeemodifyForm").data('bootstrapValidator');
            bootstrapValidator.validate();
            if(bootstrapValidator.isValid()) {
                document.getElementById("waterfeemodifyForm").submit(function(ev){ev.preventDefault();});

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
                        notEmpty: {
                            message: '手机号不能为空'
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

                        regexp:{
                            regexp:/^[0-9]{17}([0-9]|x)$/,
                            message:'请输入18位身份证号'

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
                            min: 0,
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
                            min:0,
                            max:10,
                            message:'不能超过10个字符'
                        },
                        regexp:{
                            regexp:/^[1-9]{1,3}(.[0-9]{1,2})?$/,
                            message:'输入不合法'

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
                            min: 0,
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
                            min: 0,
                            max: 4,
                            message: '最多4个字符'
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
                            max:64,
                            min:0,
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
                            min:0,
                            max:10,
                            message:'不能超过10个字符'
                        },
                        regexp:{
                            regexp:/^[1-9]{1,3}(.?[0-9]{1,2})?$/,
                            message:'输入格式不对'
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
                            min: 0,
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
                            min: 0,
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
                            min: 0,
                            max: 128,
                            message: '不能超过128个字符'
                        },


                    },

                },

                detail_houseremark:{
                    message:"输入不合法",
                    validators:{
                         stringLength:{
                            max:64,
                            min:0,
                            message:"不能超过64位"
                        }
                    }
                }


            }
        });
        ////故障报修详情表单

        $('#repairationdetailForm').bootstrapValidator({
            message:'输入不合法',
            feedbackIcons: {
                    valid: 'glyphicon glyphicon-ok',
                    invalid: 'glyphicon glyphicon-remove',
                    validating: 'glyphicon glyphicon-refresh'
                },
            fields: {
                detail_repairationestimatedcost: {
                    message:'输入不合法',
                    validators: {
                        stringLength:{
                            min:0,
                            max:8,
                            message:''
                        },
                        regexp:{
                            regexp:/^[1-9][0-9]*$/,
                            message:'输入整数'

                        }


                    }

                },
                detail_repairationactualcost:{
                     message:'输入不合法',
                    validators: {
                        stringLength:{
                            min:0,
                            max:8,
                            message:''
                        },
                        regexp:{
                            regexp:/^[1-9][0-9]*$/,
                            message:'输入整数'

                        }


                    }
                },
                detail_repairationresperson:{
                     message:'输入不合法',
                    validators: {
                        stringLength: {
                            min: 0,
                            max: 16,
                            message: '最多16位'
                        }
                    }
                },
                detail_repairationresphone: {
                    message: '输入不合法',
                    validators: {

                        stringLength: {
                            min: 0,
                            max: 11,
                            message: '11位'
                        },
                        regexp:{
                            regexp:/^[0-9]{11}$/,
                            message:'11位数字'

                        }

                    }
                },
                detail_repairationcontent:{
                    message:"输入不合法",
                    validators:{

                        stringLength: {
                            min: 0,
                            max: 128,
                            message: '不能超过128个字符'
                        },


                    },

                }
            }
        });
        ///故障报修详情
        ///////////////////////////////////////////////////////////
        ///故障报修页面
        $('#repairationForm').bootstrapValidator({
            message:'输入不合法',
            feedbackIcons: {
                    valid: 'glyphicon glyphicon-ok',
                    invalid: 'glyphicon glyphicon-remove',
                    validating: 'glyphicon glyphicon-refresh'
                },
            fields: {
                add_repairationestimatedcost: {
                    message:'输入不合法',
                    validators: {
                        notEmpty:{
                            message:"不能为空"
                        },
                        stringLength:{
                            min:0,
                            max:8,
                            message:''
                        },
                        regexp:{
                            regexp:/^[1-9][0-9]*$/,
                            message:'输入整数'

                        }


                    }

                },

                add_repairationcontent:{
                    message:"输入不合法",
                    validators:{
                        notEmpty:{
                            message:"不能为空"
                        },
                        stringLength: {
                            min: 0,
                            max: 128,
                            message: '不能超过128个字符'
                        },


                    },

                },
                add_repairationtime:{
                    message:"输入不合法",
                    validators:{
                        notEmpty:{
                            message:"不能为空"
                        }


                    },

                },


            }
        });
        ///故障报修页面
        ///////////////////////
        ///保安巡逻
        $('#patrolForm').bootstrapValidator({
            message:'输入不合法',
            feedbackIcons: {
                    valid: 'glyphicon glyphicon-ok',
                    invalid: 'glyphicon glyphicon-remove',
                    validating: 'glyphicon glyphicon-refresh'
                },
            fields: {
                patrol_eventtype: {
                    message:'输入不合法',
                    validators: {
                        notEmpty:{
                            message:"不能为空"
                        },
                        stringLength:{
                            min:0,
                            max:32,
                            message:'最多32个字符'
                        },

                    }

                },
                patrol_solveperson: {
                    message:'输入不合法',
                    validators: {
                        notEmpty:{
                            message:"不能为空"
                        },
                        stringLength:{
                            min:0,
                            max:16,
                            message:'最多16个字符'
                        },

                    }

                },

                patrol_personinvolved:{
                    message:"输入不合法",
                    validators:{
                        notEmpty:{
                            message:"不能为空"
                        },
                        stringLength: {
                            min: 0,
                            max: 16,
                            message: '最多16个字符'
                        },


                    },

                },
                patrol_phoneinvolved:{
                    message:"输入不合法",
                    validators:{
                        regexp:{
                            regexp:/^[1-9][0-9]{10}$/,
                            message:'请输入11位号码'

                        }

                    },

                },
                patrol_eventresult: {
                    message: "输入不合法",
                    validators: {
                        notEmpty: {
                            message: "不能为空"
                        },
                        stringLength: {
                            min: 0,
                            max: 32,
                            message: '最多32个字符'
                        },
                    }
                },
                patrol_eventdetail: {
                    message: "输入不合法",
                    validators: {
                        notEmpty: {
                            message: "不能为空"
                        },
                        stringLength: {
                            min: 0,
                            max: 200,
                            message: '最多200个字符'
                        },
                    }
                }


            }
        });
        ///保安巡逻页面
        ///////////////////////
        ///保安巡逻
        $('#patroldetailForm').bootstrapValidator({
            message:'输入不合法',
            feedbackIcons: {
                    valid: 'glyphicon glyphicon-ok',
                    invalid: 'glyphicon glyphicon-remove',
                    validating: 'glyphicon glyphicon-refresh'
                },
            fields: {
                patrol_detail_eventtype: {
                    message:'输入不合法',
                    validators: {
                        notEmpty:{
                            message:"不能为空"
                        },
                        stringLength:{
                            min:0,
                            max:32,
                            message:'最多32个字符'
                        },

                    }

                },
                patrol__detail_solveperson: {
                    message:'输入不合法',
                    validators: {
                        notEmpty:{
                            message:"不能为空"
                        },
                        stringLength:{
                            min:0,
                            max:16,
                            message:'最多16个字符'
                        },

                    }

                },

                patrol_detail_personinvolved:{
                    message:"输入不合法",
                    validators:{
                        notEmpty:{
                            message:"不能为空"
                        },
                        stringLength: {
                            min: 0,
                            max: 16,
                            message: '最多16个字符'
                        },


                    },

                },
                patrol_detail_phoneinvolved:{
                    message:"输入不合法",
                    validators:{
                        regexp:{
                            regexp:/^[1-9][0-9]{10}$/,
                            message:'请输入11位号码'

                        }

                    },

                },
                patrol_detail_eventresult: {
                    message: "输入不合法",
                    validators: {
                        notEmpty: {
                            message: "不能为空"
                        },
                        stringLength: {
                            min: 0,
                            max: 32,
                            message: '最多32个字符'
                        },
                    }
                },
                patrol_detail_eventdetail: {
                    message: "输入不合法",
                    validators: {
                        notEmpty: {
                            message: "不能为空"
                        },
                        stringLength: {
                            min: 0,
                            max: 200,
                            message: '最多200个字符'
                        },
                    }
                }


            }
        });
        //////////////////////////////////
         ///绿化基建
        $('#infrastructureForm').bootstrapValidator({
            message:'输入不合法',
            feedbackIcons: {
                    valid: 'glyphicon glyphicon-ok',
                    invalid: 'glyphicon glyphicon-remove',
                    validating: 'glyphicon glyphicon-refresh'
                },
            fields: {
                add_resperson: {
                    message:'输入不合法',
                    validators: {
                        notEmpty:{
                            message:"不能为空"
                        },
                        stringLength:{
                            min:0,
                            max:16,
                            message:'最多16个字符'
                        },

                    }

                },
                add_infrastructurearea: {
                    message:'输入不合法',
                    validators: {
                        notEmpty:{
                            message:"不能为空"
                        },
                        stringLength:{
                            min:0,
                            max:32,
                            message:'最多32个字符'
                        },

                    }

                },

                add_detail:{
                    message:"输入不合法",
                    validators:{
                        notEmpty:{
                            message:"不能为空"
                        },
                        stringLength: {
                            min: 0,
                            max: 200,
                            message: '最多16个字符'
                        },


                    },

                },
                add_resphone:{
                    message:"输入不合法",
                    validators:{
                        regexp:{
                            regexp:/^[1-9][0-9]{10}$/,
                            message:'11位整数'

                        }

                    },

                },



            }
        });

        ///////////////////////////
        ///绿化基建详情页
        $('#infrastructuredetailForm').bootstrapValidator({
            message:'输入不合法',
            feedbackIcons: {
                    valid: 'glyphicon glyphicon-ok',
                    invalid: 'glyphicon glyphicon-remove',
                    validating: 'glyphicon glyphicon-refresh'
                },
            fields: {
                detail_resperson: {
                    message:'输入不合法',
                    validators: {
                        notEmpty:{
                            message:"不能为空"
                        },
                        stringLength:{
                            min:0,
                            max:16,
                            message:'最多16个字符'
                        },

                    }

                },
                detail_infrastructurearea: {
                    message:'输入不合法',
                    validators: {
                        notEmpty:{
                            message:"不能为空"
                        },
                        stringLength:{
                            min:0,
                            max:32,
                            message:'最多32个字符'
                        },

                    }

                },

                detail_detail:{
                    message:"输入不合法",
                    validators:{
                        notEmpty:{
                            message:"不能为空"
                        },
                        stringLength: {
                            min: 0,
                            max: 200,
                            message: '最多16个字符'
                        },


                    },

                },
                detail_resphone:{
                    message:"输入不合法",
                    validators:{
                        regexp:{
                            regexp:/^[1-9][0-9]{10}$/,
                            message:'11位整数'

                        }

                    },

                },



            }
        });
        $('#waterfeemodifyForm').bootstrapValidator({
            message:'输入不合法',
            feedbackIcons: {
                    valid: 'glyphicon glyphicon-ok',
                    invalid: 'glyphicon glyphicon-remove',
                    validating: 'glyphicon glyphicon-refresh'
                },
            fields: {
                detail_startdegree: {
                    message:'输入不合法',
                    validators: {

                        regexp:{
                            regexp:/^[0-9]+.?[0-9]*$/,
                            message:'输入整数'

                        }


                    }

                },
                detail_enddegree: {
                    message:'输入不合法',
                    validators: {
                        regexp:{
                            regexp:/^[0-9]+.?[0-9]*$/,
                            message:'输入整数'
                        }
                    }
                }
            }
        });
        ////////////////////////
         ///员工添加
        $('#staffaddForm').bootstrapValidator({
            message:'输入不合法',
            feedbackIcons: {
                    valid: 'glyphicon glyphicon-ok',
                    invalid: 'glyphicon glyphicon-remove',
                    validating: 'glyphicon glyphicon-refresh'
                },
            fields: {
                add_staffid: {
                    message:'输入不合法',
                    validators: {
                        notEmpty:{
                            message:"不能为空"
                        },
                        stringLength:{
                            min:0,
                            max:16,
                            message:'最多16个字符'
                        },
                        regexp:{
                            regexp:/^[0-9]+$/,
                            message:"只能是数字"

                        }

                    }

                },
                add_staffname: {
                    message:'输入不合法',
                    validators: {
                        notEmpty:{
                            message:"不能为空"
                        },
                        stringLength:{
                            min:0,
                            max:32,
                            message:'最多32个字符'
                        },

                    }

                },

                add_phone:{
                    message:"输入不合法",
                    validators:{
                        notEmpty:{
                            message:"不能为空"
                        },
                        regexp:{
                            regexp:/^[0-9]{11}$/,
                            message:"11位数字"

                        }


                    },

                },
                add_idcard:{
                    message:"输入不合法",
                    validators:{
                        notEmpty:{
                            message:"不能为空"
                        },
                        regexp:{
                            regexp:/^[0-9]{17}([0-9]|[a-z])$/,
                            message:"18位数字"

                        }


                    },

                },
                add_age:{
                    message:"输入不合法",
                    validators:{
                        notEmpty:{
                            message:"不能为空"
                        },
                        stringLength:{
                            min:0,
                            max:2,
                            message:'最多2位数'
                        },
                        regexp:{
                            regexp:/^[1-9][0-9]*$/,
                            message:'2位整数'

                        }

                    },

                },
                add_job:{
                    message:"输入不合法",
                    validators:{
                        notEmpty:{
                            message:"不能为空"
                        },
                        stringLength:{
                            min:0,
                            max:18,
                            message:'最多18个字符'
                        },


                    },

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

        $('#waterfee_validateBtn').click(function() {
            $('#waterfeemodifyForm').bootstrapValidator('validate');
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
        $('#repairation_resetBtn').click(function() {
            $('#repairationForm').data('bootstrapValidator').resetForm(true);
        });
        $('#infrastructure_resetBtn').click(function() {
            $('#infrastructureForm').data('bootstrapValidator').resetForm(true);
        });


    });


