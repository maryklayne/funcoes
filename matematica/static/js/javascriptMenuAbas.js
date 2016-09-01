// JavaScript Document

$(function(){
	$('#funcoes').hide();
	var separa;	
	var hash = window.location.hash;
	if (hash !='')
	{
		separa = $(hash).html();
		$('.abas li a[href="' + hash + '"]').parent().addClass('ativo');		
	} else {
		separa = $('#funcoes div:first-child').html();			
		$('.abas li:first-child').addClass('ativo');		
	}
	$('#separa').append('<div>' + separa + '</div>').find('div').slideDown();
	$('.abas li a').click(function(){
		$('.abas li').removeClass('ativo');
		$(this).parent().addClass('ativo');
		var ancora = $(this).attr('href');
		var nome = ancora.substr(1, ancora.length);
		separa = $('#funcoes div[id="' + nome + '"]').html();
		$('#separa').empty();
		$('#separa').append('<div>' + separa + '</div>').find('div').slideDown();
	return false;
	})
})