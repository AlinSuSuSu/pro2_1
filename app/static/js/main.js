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

function finance_add(querya){

	function popup(querya){
		$('body').append('<div id="mry-opo">' +
			'<div id="mry-opo-title">' +
			'</div><div id="mry-opo-content">' +
			'<form id="finance-form" method="POST" action="/finance/waterfee/add">' +
			'<select class="ss-form-control"id="finance-houseid"name="finance-houseid">' +
			'<option></option>' +
			'</select>' +
			'</form>' +
			'</div>' +
			'</div>')
		$('#finance-form').append('<input class="ss-form-control"name="startdegree">');
		$('#finance-form').append('<input class="ss-form-control"name="enddegree">');
		$('#finance-form').append('<div id="button-area">'+
			'<input type="submit"value="确定">' +
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