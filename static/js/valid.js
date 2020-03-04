


function checkForm()
  {
    
    for (i = 0; i < $("input[name=category]").length; i++) {
        if ($("input[name=category]")[i].checked) {
          
          return true;
        }
        
    } 
    alert("Select at least one Category");  
    return false;  
    
  }
 

