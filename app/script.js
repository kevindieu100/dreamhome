function search(element) {
	if (event.keyCode == 13) {
		//alert(element.value);
		document.getElementById("name").innerHTML = "Hello, " + element.value;
		document.getElementById("name").style.fontSize = "40pt";
		document.getElementById("name").style.paddingTop = "10pt";
		document.getElementById("name").innerHTML += "<div id='sub'><input type='Submit' value='Find Dream Home' onclick='move()'></div>";
	}
}
function move() {
	window.location.href = "file:///C:/Users/Sony/Desktop/Projects/HACKSC/dreamhome/app/survey.html";
}