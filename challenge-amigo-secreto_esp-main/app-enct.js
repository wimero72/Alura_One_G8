function show(message) {
    document.querySelector("#output").innerHTML=message;
    }
    
    function updateWeb() {
        document.querySelector("#empty").style.display="none";
        document.querySelector("#emptytxtimage").style.display="none";
        document.querySelector("#noMsg").style.display="none";
        document.querySelector("#noMsgParagraph").style.display="none";
        document.querySelector("#output").style.display="inline-block";
        document.querySelector("#copy").style.display="inline-block";
        
    }
    
    function encryption() {
        var message=document.querySelector("#text").value;
        var key="";
    
        if (message!= "" && !/[A-Z]/g.test(message) && !/[á-ú]/g.test(message) && message.trim().length) {
            for(var i=0; i<message.length;i++) {
                switch(message[i]) {
                    case "a":
                        key+="ai";
                        break;
                    case "e":
                        key+="enter";
                        break;
                    case "i":
                        key+="imes";
                        break;
                    case "o":
                        key+="ober";
                        break;
                    case "u":
                        key+="ufat";
                        break;
                    default:
                        key+=message[i];
                }
            }
    
            updateWeb();
            show(key);
            document.querySelector('#text').value='';
            }
    
        else { 
            alert("Por favor, utilice solo minúsculas y sin acentos");
            }
        }
    
    function decryption(){
        var message = document.querySelector("#text").value;
        var keys= [/ai/g, /enter/g, /imes/g, /ober/g, /ufat/g];
        var vowels = ['a','e','i','o','u'];
        
        if(message!="" && !/[A-Z]/g.test(message) && !/[á-ú]/g.test(message) && message.trim().length){
            for(var i=0;i<5;i++){
                message=message.replaceAll(keys[i], vowels[i]);
            }
    
            updateWeb();
            show(message);
            document.querySelector('#text').value='';
        }
    
        else { alert("Por favor, utilice solo minúsculas y sin acentos"); 
    
        }
        
    }    
    
    function copyText(){
        var text = document.querySelector("#output");
        text.select();
        text.setSelectionRange(0, 99999); /* Sólo móviles */
        navigator.clipboard.writeText(text.value);
    }
    
    var encrypt = document.querySelector("#encrypt");
    var decrypt = document.querySelector("#decrypt");
    var copy = document.querySelector("#copy");
    
    
    copy.onclick = copyText;
    encrypt.onclick = encryption;
    decrypt.onclick = decryption;