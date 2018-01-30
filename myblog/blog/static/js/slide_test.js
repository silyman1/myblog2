var slideIndex = 0;
var flag =true
showSlides();

function showSlides(){
	var i;
	var slides =document.getElementsByClassName("slideshow");
	for (i=0;i<slides.length;i++){
		slides[i].style.display ="none";
	}
	slideIndex++;
	if(slideIndex>slides.length){slideIndex=1}
	slides[slideIndex-1].style.display="block";
	t = setTimeout(showSlides,3500);
}
function stopSlides(t){
	if (flag){
	clearTimeout(t);
	document.getElementById('flag').innerHTML = 'play'
	}
	else{
		t = setTimeout(showSlides,3500);
		document.getElementById('flag').innerHTML = 'stop'
	}
	flag =!flag;
}
function jumpTo(n){
	if (flag){
	clearTimeout(t);
	document.getElementById('flag').innerHTML = 'play'
	flag =!flag;
	}
	var slides =document.getElementsByClassName("slideshow");
	for (i=0;i<slides.length;i++){
		slides[i].style.display ="none";
	}
	slides[n-1].style.display="block";
}