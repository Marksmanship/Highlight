var windowWidth = document.getElementsByClassName('Main-Content')[0].clientWidth;
var imgContainer = document.getElementsByClassName('Background-Image-Container')[0];


imgContainer.addEventListener('mousemove', function(){
  var moveX = document.getElementsByClassName('Main-Content')[0].clientWidth;
      moveX = ((moveX / 2) - event.pageX) * .035;
  var moveY = document.getElementsByClassName('Main-Content')[0].clientHeight;
      moveY = ((moveY / 2) - event.pageY) * .035;

  imgContainer.style.marginLeft = moveX + "px";
  imgContainer.style.marginTop = moveY + "px";
});



var tabButtons = document.querySelectorAll(".Button-Wrapper button");
var tabPanels = document.querySelectorAll(".Tab-Panel");
document.querySelectorAll('.Tab-Panel')[1].style.display = "none";

function showPanel(panelIndex, colorCode)
{
  tabButtons.forEach(function(node)
  {
    node.style.backgroundColor='#2D3C49';
    node.style.color="darkgrey";
  });
  tabPanels[panelIndex].style.display = "block";
  tabButtons[panelIndex].style.backgroundColor=colorCode;
  tabButtons[panelIndex].style.color='#FFFFFF';
  (panelIndex == 0) ? tabPanels[1].style.display = "none" : tabPanels[0].style.display = "none";
}
function checkForm()
{
  if (form.inputfield.value == "")
  {
    alert("Error: Input is empty!");
    form.inputfield.focus();
    return false;
  }
}
/*
var registerScreenWrapper = document.getElementsByClassName('Register-Screen-Wrapper')[0];
var registerContainer = document.getElementsByClassName('Register-Container')[0];
function MoveTo() // Shift the transparent background
{
  registerScreenWrapper.classList.toggle('Active-Screen-Wrapper');
  registerContainer.classList.toggle('Active-Container');
  document.querySelectorAll(".Main-Image-Container > img")[0].classList.toggle("blur");

  TriggerOpacity(registerContainer);	// Toggle the opacity manager

}
function TriggerOpacity(elm)
{
  if (elm.style.opacity == 0)							// If the element is already invisible
  {
    console.log("Opacity initially equals 0. Setting to 1.");
    elm.style.opacity = 1.0;							// Make is visible
    TriggerDisplay(1.0);									// Call function to set display to block
  }
  else if (elm.style.opacity == 1)					// If the element is already visible
  {
    console.log("Opacity initially equals 1.0. Setting to 0.");
    elm.style.opacity= 0.0; 							// Make it invisible
    TriggerDisplay(0.0);									// Call function to set display to hidden
  }
  else { alert("error in TriggerOpacity."); }
}
function TriggerDisplay(value)
{
  switch(value)
  {
    case 0.0:
      console.log("Setting dispay:none");
      registerContainer.style.display = "none";
      AddForms();
      break;
    case 1.0:
      console.log("Setting display:block");
      registerContainer.style.display = "block";
      break;
    default:
      console.log("Error in passed opacity value.");

  }
}
function AddForms()
{
  var screen = document.getElementsByClassName('Register-Screen-Wrapper')[0];
  screen.insertAdjacentHTML("afterend", "<form class='Not-Visible' id='created-form' style='-webkit-transition: 1.2s; position: absolute; z-index: 3; top: 22vh; left: 44.5%;transform: translateX(-50%); margin: 20px 0; width: 350px; color: steelblue;'><input type='email' placeholder='Email' style='padding: 10px; font-size: inherit; display: block; margin-bottom: 25px; width: 100%; border: 2px solid steelblue; border-radius: 3px;'><input type='password' placeholder='Password' style='padding: 10px; font-size: inherit; display: block; margin-bottom: 25px; width: 100%; border: 2px solid steelblue; border-radius: 3px;'><input type='submit' name='Submit' value='Log In' style='width: 75px; height: 45px; border-radius: 3px; border: none; background-color: #509B65; margin: 0 auto; position: absolute; left: 50%; transform: translateX(-50%); color: white; text-transform: uppercase;'></form>");
  screen.insertAdjacentHTML("afterend", "<div id='login-summary' style='position: absolute; z-index: 4; top: 10vh; left: 45%;transform: translateX(-50%);color: white; text-align: center; opacity: 1.0 !important;'><h1 style='width: 50%; margin: 4% auto 0 auto; font-size: 250%; text-shadow: 4px 4px 2px rgba(0, 0, 0, 0.48);'>Login</h1><p style='font-size: 160%; text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.25);'>to your HighlightPage account!</p>");
  document.getElementById('created-form').classList.toggle('Now-Visible');
}*/
