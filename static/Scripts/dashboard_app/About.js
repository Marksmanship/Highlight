let itemList = document.querySelectorAll('.Card');
let leftArrow = document.querySelector('#left-arrow');
let rightArrow = document.querySelector('#right-arrow');
let currentIndex = 0;



/* Based off the assumption that there are at least 4 items */
leftArrow.addEventListener("click", function()
{
  if (currentIndex === 0)
  {
    currentIndex = itemList.length;
  }

  slideLeft();
});
function slideLeft()
{
  var moveBy = 215 * (currentIndex-1);    // 10 -1 = 9 * 860? No.
  for (var i = itemList.length -1; i >= 0; i--)
  {
    itemList[i].style.transform = "translateX(" +"-"+ moveBy + "px)";
  }

  currentIndex -= 1 // -= 3 + (itemList.length % 4);
}

rightArrow.addEventListener("click", function()
{
  if (currentIndex === itemList.length-1)
  {
    currentIndex = -1;
  }
  slideRight();
});
function slideRight()
{
  var moveBy = 215 * (currentIndex+1);
  for (var i = 0; i < itemList.length; i++)
  {
    itemList[i].style.transform = "translateX("+ "-" + moveBy + "px)";
  }
  currentIndex += 1;
}
/*
  /* var radioButtons = document.querySelectorAll('input[type="radio"]');
for (var i = 0; i < radioButtons.length; i ++)
{
  /* By iteration, Initialize all unchecked labels to display:none
  if (radioButtons[i].checked == false)
  {
    var elmName = radioButtons[i].id;
    var setToNone = document.querySelectorAll("label#" + elmName)[0];
    // setToNone.style.display = "none";
  }
  radioButtons[i].addEventListener("click", function() /* Once the user clicks on a tab
  {
    if (this.checked == true)
    {
      var trueName = this.id;
      console.log(trueName);
      document.querySelectorAll("label#" + trueName).style.display = "block";

      var notChecked = document.querySelectorAll("label:not(#" + trueName + ")");
      for (var j = 0; j < notChecked.length; j++)
      {
        console.log(notChecked[j].id + " is inactive.");
        notChecked[j].style.display = "none";
      }
    }
  });
}*/
