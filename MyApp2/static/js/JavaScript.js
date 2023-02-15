window.onload = function () {
	var s;
	var timer;

	document.getElementById("top").onclick = function () {
		s = window.pageYOffest;
		sto();
	}

	function sto() {
		if (s > 0) {
			window.scrollTo(0, s);
			s = s - 100;

			timer = setTymeout(sto, 100);
		}
		else { clearTymeout(timer); window.scrollTo(0, 0); }
	}

}


function style_ch() {
	alert("adsadad");
	var bod = document.getElementById('bod');
	bod.style.backgroundImage = "url('https://github.com/notname123456789/my-first-blog/blob/main/MyApp2/static/media/2.jpg?raw=true')";
	var art = document.getElementById('art');
	art.style.backgroundColor = "#1F2833";
	var art = document.getElementById('s1');
	art.style.backgroundColor = "#1F2833";
	var art = document.getElementById('s2');
	art.style.backgroundColor = "#1F2833";
	s = document.getElementsByClassName('s');
	s.style.backgroundColor = "red";
}

