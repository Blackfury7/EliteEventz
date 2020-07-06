function signup(){
var xhttp = new XMLHttpRequest();
  var a;
xhttp.onreadystatechange = function() {
  	console.log(this.readyState);
  	 console.log(this.status);
    if (this.readyState == 4 && this.status == 200) {

    a = JSON.parse(this.responseText);
    alert(a);
	}
  };
	var name=document.querySelector('#name').value;
var username=document.getElementById("username").value;
	var email=document.querySelector('#email').value;
	var password=document.querySelector('#password').value;

 	   var myJSON = JSON.stringify({"name":name, "username": username ,"email":email, "password": password });
// console.log(myJSON);
xhttp.open("POST", "http://127.0.0.1:8000/signup/customer/", true);
  xhttp.send(myJSON);
}