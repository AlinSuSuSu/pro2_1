/**
 * Created by Administrator on 2017-03-17.
 */


$('.pm-staffmessage').click(function () {
	$('.pm-staffmessage').addClass('active');
	$('.pm-staffbonus').removeClass('active');
	$('.pm-holiday').removeClass('active');
	$('.pm-reimbursement').removeClass('active');
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

$('a.ss-table-delete-staff').on('click',function(evt){
	evt.preventDefault();
	var staff_id = $(this).attr('id');
	$.ajax({
		url:'/staff/staff_message/delete/'+staff_id,
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


function finance_add(querya){

	function popup(querya){
		$('body').append('<div id="mry-opo">' +
			'<div id="mry-opo-title">' +
			'</div><div id="mry-opo-content">' +
			'<form id="finance-form" method="POST" action="/finance/waterfee/add">' +
			'<div class="col-lg-4"><select class="form-control"id="finance-houseid"name="finance-houseid">' +
			'<option></option>' +
			'</select></div>' +
			'</form>' +
			'</div>' +
			'</div>')
		$('#finance-form').append('<div class="col-lg-4"><input class="form-control "name="startdegree"placeholder="起始度数"></div>');
		$('#finance-form').append('<div class="col-lg-4"><input class="form-control "name="startdate"placeholder="起始时间"></div>');
		$('#finance-form').append('<div id="button-areaa">'+
			'<input type="reset"class="btn btn-info col-lg-offset-4 button-area"id="water_reset"value="重置">' +
			'<input type="submit"class="btn btn-info col-lg-offset-1 button-area"id="water_validate"value="确定">' +
			'</div>')
		var div = $('#mry-opo');
        $('#mry-opo-title').text('添加业主水费记录');
        for(var k in querya){
		$('#finance-houseid').append("<option value='"+querya[k]+"'>"+querya[k]+"</option>");
		}
        div.css('width', 500 + 'px');
        div.css('height', 200 + 'px');
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
function waterfee_save(waterfeeid){
	startdegree=document.getElementById(waterfeeid).setAttribute('background','#eeeeaa');
}
function waterfee_focus(waterfeeid){
	startdegree=document.getElementById(waterfeeid).setAttribute('background','#aeeef');



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