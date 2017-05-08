/**
 * Created by Administrator on 2017-03-17.
 */
/*

$('.house').click(function () {
	$('.house').addClass('nav-active');
	$('.owner').removeClass('nav-active');
	$('#line').addClass('one');
	$('#line').removeClass('two');
	$('#line').removeClass('three');
	$('#line').removeClass('four');
});
$('.pm-staffbonus').click(function () {
	$('.pm-staffbonus').addClass('active');
	$('.pm-staffmessage').removeClass('active');
	$('.pm-holiday').removeClass('active');
	$('.pm-reimbursement').removeClass('active');
	$('#line').addClass('two');
	$('#line').removeClass('one');
	$('#line').removeClass('three');
	$('#line').removeClass('four');
});
$('.pm-holiday').click(function () {
	$('.pm-holiday').addClass('active');
	$('.pm-staffbonus').removeClass('active');
	$('.pm-staffmessage').removeClass('active');
	$('.pm-reimbursement').removeClass('active');
	$('#line').addClass('three');
	$('#line').removeClass('two');
	$('#line').removeClass('one');
	$('#line').removeClass('four');
});
$('.pm-reimbursement').click(function () {
	$('.pm-reimbursement').addClass('active');
	$('.pm-staffbonus').removeClass('active');
	$('.pm-holiday').removeClass('active');
	$('.pm-staffmessage').removeClass('active');
	$('#line').addClass('four');
	$('#line').removeClass('two');
	$('#line').removeClass('three');
	$('#line').removeClass('one');
});
$('.pm-staffmessage').click(function () {
	$('#first').addClass('active');
	$('#second').removeClass('active');
	$('#third').removeClass('active');
	$('#fourth').removeClass('active');
});
$('.pm-staffbonus').click(function () {
	$('#first').removeClass('active');
	$('#second').addClass('active');
	$('#third').removeClass('active');
	$('#fourth').removeClass('active');
});
$('.pm-holiday').click(function () {
	$('#first').removeClass('active');
	$('#second').removeClass('active');
	$('#third').addClass('active');
	$('#fourth').removeClass('active');
});
$('.pm-reimbursement').click(function () {
	$('#first').removeClass('active');
	$('#second').removeClass('active');
	$('#third').removeClass('active');
	$('#fourth').addClass('active');
});
*/

$('a.ss-table-delete-staff').on('click',function(evt){
	evt.preventDefault();
	var staffid = $(this).attr('id');
	$.ajax({
		url:'/setting/staff/delete/'+staffid,
		type:'POST',
		dataType:'JSON',
		success:function(resp){
			if(resp.status != 1){
				alert("删除失败："+resp.message);
			}
			location.reload()
		}
	})
})

$('a.ss-table-delete-choice').on('click',function(evt){
	evt.preventDefault();
	var id = $(this).attr('id');
	$.ajax({
		url:'/setting/choice/delete/'+id,
		type:'POST',
		dataType:'JSON',
		success:function(resp){
			if(resp.status != 1){
				alert("删除失败："+resp.message);
			}
			location.reload()
		}
	})
})

$('a.ss-table-delete-house').on('click',function(evt){
	evt.preventDefault();
	var house_id = $(this).attr('id');
	$.ajax({
		url:'/house/house_message/delete/'+house_id,
		type:'POST',
		dataType:'JSON',
		success:function(resp){
			if(resp.status != 1){
				alert("删除失败："+resp.message);
			}
			location.reload()
		}
	})
})

$('a.ss-table-delete-owner').on('click',function(evt){
	evt.preventDefault();
	var house_id = $(this).attr('id');
	$.ajax({
		url:'/house/house_owner/delete/'+house_id,
		type:'POST',
		dataType:'JSON',
		success:function(resp){
			if(resp.status != 1){
				alert("删除失败："+resp.message);
			}
			location.reload()
		}
	})
})

$('a.ss-table-delete-repairation').on('click',function(evt){
	evt.preventDefault();
	var repairationid = $(this).attr('id');
	$.ajax({
		url:'/community/repairation/delete/'+repairationid,
		type:'POST',
		dataType:'JSON',
		success:function(resp){
			if(resp.status != 1){
				alert("删除失败："+resp.message);
			}
			location.reload()
		}
	})
})

$('a.ss-table-delete-patrol').on('click',function(evt){
	evt.preventDefault();
	var patrolid = $(this).attr('id');
	$.ajax({
		url:'/community/patrol/delete/'+patrolid,
		type:'POST',
		dataType:'JSON',
		success:function(resp){
			if(resp.status != 1){
				alert("删除失败："+resp.message);
			}
			location.reload()
		}
	})
})
$('a.ss-table-delete-infrastructure').on('click',function(evt){
	evt.preventDefault();
	var infrastructureid = $(this).attr('id');
	$.ajax({
		url:'/community/infrastructure/delete/'+infrastructureid,
		type:'POST',
		dataType:'JSON',
		success:function(resp){
			if(resp.status != 1){
				alert("删除失败："+resp.message);
			}
			location.reload()
		}
	})
})
$('a.ss-table-delete-complaint').on('click',function(evt){
	evt.preventDefault();
	var complaintid = $(this).attr('id');
	$.ajax({
		url:'/community/complaint/delete/'+complaintid,
		type:'POST',
		dataType:'JSON',
		success:function(resp){
			if(resp.status != 1){
				alert("删除失败："+resp.message);
			}
			location.reload()
		}
	})
})
$('a.ss-table-delete-waterfee').on('click',function(evt){
	evt.preventDefault();
	var waterfeeid = $(this).attr('id');
	$.ajax({
		url:'/finance/waterfee/delete/'+waterfeeid,
		type:'POST',
		dataType:'JSON',
		success:function(resp){
			if(resp.status != 1){
				alert("删除失败："+resp.message);
			}
			location.reload()
		}
	})
})


$('a.ss-table-delete-electricfee').on('click',function(evt){
	evt.preventDefault();
	var electricfeeid = $(this).attr('id');
	$.ajax({
		url:'/finance/electricfee/delete/'+electricfeeid,
		type:'POST',
		dataType:'JSON',
		success:function(resp){
			if(resp.status != 1){
				alert("删除失败："+resp.message);
			}
			location.reload()
		}
	})
})
$('a.ss-table-delete-gasfee').on('click',function(evt){
	evt.preventDefault();
	var gasfeeid = $(this).attr('id');
	$.ajax({
		url:'/finance/gasfee/delete/'+gasfeeid,
		type:'POST',
		dataType:'JSON',
		success:function(resp){
			if(resp.status != 1){
				alert("删除失败："+resp.message);
			}
			location.reload()
		}
	})
})
$('a.ss-table-delete-cleaningfee').on('click',function(evt){
	evt.preventDefault();
	var cleaningfeeid = $(this).attr('id');
	$.ajax({
		url:'/finance/cleaningfee/delete/'+cleaningfeeid,
		type:'POST',
		dataType:'JSON',
		success:function(resp){
			if(resp.status != 1){
				alert("删除失败："+resp.message);
			}
			location.reload()
		}
	})
})
function finance_add(querya){

	function popup(querya){
		$('body').append('<div id="mry-opo">' +
			'<div id="mry-opo-title">' +
			'</div><div id="mry-opo-content">' +
			'<form id="finance-form"class="form-inline"method="POST" action="/finance/add">' +
			'<div class="form-group col-md-9"><label class="col-md-4 control-label">房产编号</label><div class="col-md-6"><select class="form-control"id="finance-houseid"name="finance-houseid">' +
			'<option></option>' +
			'</select></div></div>' +
			'<div class="form-group col-md-9"><label class="col-md-4 control-label">收费项目</label><div class="col-md-6"><select class="form-control"name="type"><option value="水费">水费</option><option value="电费">电费</option><option value="天然气费">天然气费</option><option value="卫生费">卫生费</option></select></div></div>'+
			'</form>' +
			'</div>' +
			'</div>')
		$('#finance-form').append('<div class="col-md-9 form-group"><label class="col-md-4 control-label">进户日期</label>'+
                        	'<div class="input-group date form_date col-md-7" data-date="" data-date-format="yyyy-mm-dd  " data-link-field="dtp_input2" data-link-format="yyyy-mm-dd">'+
                            '<input class="form-control" size="12" type="text" name="startdate" readonly>'+
                            '<span class="input-group-addon"><span class="glyphicon glyphicon-remove"></span></span>'+
                            '<span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>'+
                        '<input type="hidden" id="dtp_input2" value="" />'+
                    '</div>');
		$('#finance-form').append('<div id="button-areaa">'+
			'<input type="reset"class="btn btn-info col-lg-offset-4 button-area"id="water_reset"value="重置">' +
			'<input type="submit"class="btn btn-info col-lg-offset-1 button-area"id="water_validate"value="确定">' +
			'</div>')
		var div = $('#mry-opo');
        $('#mry-opo-title').text('添加收费记录');
        for(var k in querya){
		$('#finance-houseid').append("<option value='"+querya[k]+"'>"+querya[k]+"</option>");
		}
		new_element=document.createElement("script");
		new_element.setAttribute("type","text/javascript");
		new_element.setAttribute("src","../static/js/bootstrap-datetimepicker.js");
		document.body.appendChild(new_element);
		$('body').append("<script>$('.form_date').datetimepicker({"+
        "weekStart: 1,"+
        "todayBtn:  1,"+
		"autoclose: 1,"+
		"todayHighlight: 1,"+
		"startView: 2,"+
		"minView: 2,"+
		"forceParse: 0"+
    	"});</script>");
        div.css('width', 500 + 'px');
        div.css('height', 300 + 'px');
        div.css('margin-left', -(parseInt(500) / 2) + 'px');
        div.css('margin-top', -(parseInt(200) / 2) + 'px');
        div.css('background', '#fff');
        $('#mry-mask').css('display', 'block');
	}
	function del() {
        $('#mry-opo').append('<a href="javascript:void(0)" deletes="mry-opo" style="position:absolute;right:10px;top:6px;color:#fff;font-size:12px;">X</a>');
        $('[deletes=mry-opo]').click(function() {
            $('#mry-opo,#mry-mask').remove();
        });
    }
    $('body').append('<div id="mry-mask" deletes="mry-opo"></div>');
	popup(querya);
	del();
}
function waterfee_modify(waterfeeid){
	$("#input_td input").attr("readonly",false);
	$("#input_td input").css("background","#aaddee");


}

/*
function waterfee_save(waterfeeid){
	document.getElementById(waterfeeid).setAttribute('background','#eeeeaa');
}
function waterfee_focus(this){
	document.getElementById(waterfeeid).setAttribute('background','#aeeef');



}
/*
function waterfee_create(query_waterfee){
	function create(query_waterfee){
		var date = new Date();

		if(query_waterfee){
			if(parseInt(query_waterfee[0].substr(0,4))==date.getFullYear()&&parseInt(query_waterfee[0].substr(4,2)==date.getMonth()) ){
					alert('已经生成过本月的明细账单');
			}

		}
		else{
			$.ajax({
				url:'/finance/waterfee/create',
				type:'POST',
				dataType:'JSON',
				success:function(resp) {
                    if (resp.status != 1) {
                        alert("生成失败：" + resp.message);
                    }
                    location.reload()
                }
				})
		}

	}
	 create(query_waterfee);

}*/