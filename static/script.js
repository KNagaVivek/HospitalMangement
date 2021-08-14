
function appointment_check() {
  var n = document.getElementById('apname').value;
	var pn = document.getElementById('apnum').value;
  var pr = document.getElementById('approb').value;
	
	var regn = /^([a-z]){5,50}$/i;
	// var re = /^([a-z 0-9 \. -])+@([a-z])+.([a-z 0-9]){2,8}(.[a-z 0-9]{2,8})?$/i;
	// var rp  = /^([\w @ $]){6,20}$/i;
  var rprob=/^[\w / ]+$/
  var rpn = /^[7-9]\d{9}$/;

  document.getElementById('er1').style.visibility="hidden";
  document.getElementById('er2').style.visibility="hidden";
  document.getElementById('er3').style.visibility="hidden";

  
  if(!regn.test(n)) {
    document.getElementById('er1').style.visibility="visible";
    return false;
  }
  if(!rpn.test(pn)) {
    document.getElementById('er2').style.visibility="visible";
    return false;
  } 
  if(!rprob.test(pr)) {
    document.getElementById('er3').style.visibility="visible";
    return false;
  } 

}

function check_login() {
  var fn = document.getElementById('fname').value.trim();
	var ln = document.getElementById('lname').value.trim();
  var un = document.getElementById('uname').value;
	var pas = document.getElementById('psw').value;
  var pas2 = document.getElementById('psw2').value;
	var em = document.getElementById('email').value;
  var pn = document.getElementById('number').value;

  var regn = /^([a-z ])+$/i;
	var re = /^([a-z 0-9 \. -])+@([a-z])+.([a-z 0-9]){2,8}(.[a-z 0-9]{2,8})?$/i;
	var rp  = /^([\w @ $]){8,20}$/i;
  var ru=/^[\w @ $]{6,30}$/
  var rpn = /^[6-9]\d{9}$/;

  document.getElementById('er01').style.visibility="hidden";
  document.getElementById('er02').style.visibility="hidden";
  document.getElementById('er03').style.visibility="hidden";
  document.getElementById('er04').style.visibility="hidden";
  document.getElementById('er05').style.visibility="hidden";
  document.getElementById('er06').style.visibility="hidden";
  document.getElementById('er07').style.visibility="hidden";

  if(!regn.test(fn)) {
    document.getElementById('er01').style.visibility="visible";
    return false;
  }

  if(!regn.test(ln)) {
    document.getElementById('er02').style.visibility="visible";
    return false;
  }

  if(!ru.test(un)) {
    document.getElementById('er03').style.visibility="visible";
    return false;
  }

  if(!rp.test(pas)) {
    document.getElementById('er04').style.visibility="visible";
    return false;
  }

  if(!rp.test(pas2)) {
    document.getElementById('er05').style.visibility="visible";
    if(pas != pas2) {
      document.getElementById('er05').style.visibility="visible";
      document.getElementById('er05').innerHTML="Password should not match";
    }
    return false;
  }

  if(!re.test(em)) {
    document.getElementById('er06').style.visibility="visible";
    return false;
  }

  if(!rpn.test(pn)) {
    document.getElementById('er07').style.visibility="visible";
    return false;
  }
}