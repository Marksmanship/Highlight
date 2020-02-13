const upArrow = document.getElementById('up-arrow');
const downArrow = document.getElementById('down-arrow');
const tables = document.getElementsByClassName('cta-sport-table')

/* When moving down, you want your current and above elements to move up;
   When moving up, you want your current and above elements to move down */

let currentIndex = 0;
const moveBy = 210;
const arrayLength = tables.length -1;
upArrow.addEventListener("click", function(){
	if (currentIndex >= 0 && currentIndex <= arrayLength)
	{
		// From top to bottom, increase each element's margin by the number of items below it
		if (currentIndex == 0)
		{
			for (i = 0; i < arrayLength; i++)
			{
				tables[i].style.marginTop = (i - arrayLength) * moveBy + "px";
			}
			currentIndex = arrayLength;
		}
		else
		{
			// Want each element ABOVE the currentIndex to move down at a constant rate without subtracting from the currently stored value.
			// To do this, we must take the index of all elements above the currentIndex, and subtract if from whatever index preceeds the currentIndex.
			// We then set the margin. Say currentIndex equals 3: i would equal 2, so 2-(3-1) = 0. We just made our element of index 2, get a margin of 0 (currentIndex).
			// And this happens until we reach element of index 0, in which case another statement handles its margin.
			for (i = currentIndex-1; i >= 0; i--)
			{
				tables[i].style.marginTop = (i-(currentIndex-1)) * moveBy + "px";
			}
			currentIndex -=1;
		}
	}
});

downArrow.addEventListener('click', function(){
	if (currentIndex >= 0 && currentIndex <= arrayLength)
	{
		// All-case -- we want something to happen to every element so we don't have to start at currentIndex
		if (currentIndex == arrayLength)
		{
			for (i=0; i <= arrayLength; i++)
			{
				tables[i].style.marginTop = 0 + "px";
			}
			currentIndex = 0;
		}
		// Ideally, we'd want each element below the current index to shift upward, but that would require us to set margins on elements below the curIndex, which we've avoid so far
		// Instead, we'll move each element above the current index, above one space. The default behavior of the elements below the curIndex is to fill in that gap.
		else
		{
			for (i = currentIndex; i >= 0; i--)
			{
				tables[i].style.marginTop = (i - (currentIndex+1)) * moveBy + "px";
			}
			currentIndex +=1
		}
	}
});
