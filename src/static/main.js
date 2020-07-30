var ourReq = new XMLHttpRequest();
ourReq.open('GET','http://127.0.0.1:8000/drf/employee');
ourReq.onload = function (){
    console.log(ourReq.responseText);
};
ourReq.send();