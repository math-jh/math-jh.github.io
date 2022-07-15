$(function(){
  // When page loads, wait 3 seconds and hide all elements with .top_button class:
  setTimeout(toggle, 3000);
});

var timer = null;

// General function for adding/removing the "hide" class.
// This is used when the page first loads and each time
// the mouse moves on the page. We're not calling toggle()
// here because a flicker effect can happen which would leave
// the elements showing instead of being hidden.
function toggle(){
  $('.top_button').toggleClass('hide');
}

$(window).on('mousemove', function(){
  // When anywhere on page is moused over bring back .top_button
  // elements for 3 seconds. Removing "hide" simply restores
  // the original CSS & layout
  $('.top_button').removeClass('hide');
  
  // Kill any previous timers
  clearTimeout(timer);
  
  // Wait 3 seconds and hide again
  timer = setTimeout(toggle, 3000)
});
