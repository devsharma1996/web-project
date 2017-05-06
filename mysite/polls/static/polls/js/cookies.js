function createCookie(type,product){
    
        if(getCookie(type).length!==0){
            return;
        }
        var no;
        console.log(type);
        console.log(product);
        var allcookies = document.cookie;
        cookiearray = allcookies.split(';');
        console.log(allcookies);
        console.log(cookiearray.length);
        if(getCookie('no').length==0){
            no=0;
            document.cookie="no="+no+";";
            console.log("enterd the if")
        }
        ReadCookie();
        no=parseInt(getCookie('no'))+1;
        document.cookie="no="+no+";";
        document.cookie=type+"="+product+";";
        document.getElementById("no_of_products").textContent=no;
        allcookies=document.cookie;
        console.log(allcookies);
}

function ReadCookie()
            {
               var allcookies = document.cookie;
               console.log(allcookies);
               cookiearray = allcookies.split(';');
               for(var i=0; i<cookiearray.length; i++){
                  name = cookiearray[i].split('=')[0];
                  value = cookiearray[i].split('=')[1];
                  console.log(name);
                  console.log(value);
               }
            }

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}