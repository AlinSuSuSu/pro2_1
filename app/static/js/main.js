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


$('#searchmessage').click(function(){
	var data={
		'staffid':$('#staffid').val(),
		'staffname':$('#staffname').val(),
		'staffgender':$("input[name='gender']:checked").val()
	};
	$.ajax({
		type:'GET',
		url:'/',
		data:data,
		dataType:'json',
		contentType:"application/json;charset='UTF-8'",
		success: function(data) {

		},
	})
});
$('a.ss-table-delete').on('click',function(evt){
	evt.preventDefault();
	var staff_id = $(this).attr('id');
	$.ajax({
		url:'/detail/delete/'+staff_id,
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