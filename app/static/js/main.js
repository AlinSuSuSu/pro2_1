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
