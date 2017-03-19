/**
 * Created by Administrator on 2017-03-17.
 */
/**$(function(){
          function footerPosition(){
              $("footer").removeClass("fixed-bottom");
              var contentHeight = document.body.scrollHeight,//网页正文全文高度
                  winHeight = window.innerHeight;//可视窗口高度，不包括浏览器顶部工具栏
              if(!(contentHeight > winHeight)){
                  //当网页正文高度小于可视窗口高度时，为footer添加类fixed-bottom
                  $("footer").addClass("fixed-bottom");
              } else {
                  $("footer").removeClass("fixed-bottom");
              }
          }
          footerPosition();
          $(window).resize(footerPosition);
      });
**/
/**
$(function(){
 var Accordion = function(el, multiple) {
  this.el = el || {};
  this.multiple = multiple || false;
  // Variables privadas
  var links = this.el.find('.link');
  // Evento
  links.on('click', {el: this.el, multiple: this.multiple}, this.dropdown)
 }
 Accordion.prototype.dropdown = function(e) {
  var $el = e.data.el;
   $this = $(this),
   $next = $this.next();

  $next.slideToggle();
  $this.parent().toggleClass('open');

  if (!e.data.multiple) {
   $el.find('.submenu').not($next).slideUp().parent().removeClass('open');
  };
 }
 var accordion = new Accordion($('#accordion'), false);
});
**/

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