// function togglePopup(id) {
//   var popup = document.getElementById('popup' + id);
//   if (popup.style.display === 'block') {
//     popup.style.display = 'none';
//   } else {
//     popup.style.display = 'block';
//   }
// }

function togglePopup(spiralid) {
    var popup = document.getElementById('popup' + spiralid);
    if (popup.style.display === 'block') {
      popup.style.display = 'none';
      resetButtonLayoutPopup(); // Reset button layout when popup is hidden
    } else {
      popup.style.display = 'block';
      adjustButtonLayoutPopup(spiralid); // Adjust button layout when popup is displayed
    }
  }
  
  function adjustButtonLayoutPopup(spiralid) {
    var buttons = document.getElementsByClassName('section-btn');
    for (var i = spiralid+1; i < buttons.length; i++) {
      buttons[i].style.marginTop = '280px'; // Adjust margin top to create space for the popup
    }
  }
  
  function resetButtonLayoutPopup() {
    var buttons = document.getElementsByClassName('section-btn');
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].style.marginTop = '0'; // Reset margin top to default value
    }
  }

//   Milestones function 

  function toggleMilestone(spiralid,milestoneid){
    var milestonepopup = document.getElementById('milestonepopup' +spiralid +milestoneid);
    if(milestonepopup.style.display==='block'){
        milestonepopup.style.display= 'none';
        // resetButtonLayoutMilestone();
    }
    else{
        milestonepopup.style.display = 'block';
        // adjustButtonLayoutMilestone(milestoneid);
    }

  }

 


