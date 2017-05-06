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
