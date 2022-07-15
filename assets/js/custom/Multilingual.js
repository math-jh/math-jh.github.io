function lang_home() {
    var origin = window.location.origin;
    var pathname = window.location.pathname.split('/');
    if (pathname[1] == "en" || pathname[1] == "ko"){
        window.location.href = "/" + pathname[1];
    }
    else {
        window.location.href = "/"
    }
}

function lang_select() {
    var pathname = window.location.pathname.split('/');
    var newpathname = "";
    if (pathname[1] == "en") {
      var newlang = "/ko";
    } else if (pathname[1] == "ko") {
      var newlang = "/en";
    }
    for (i = 2; i < pathname.length; i++) {
      newpathname += "/";
      newpathname += pathname[i];
    }
    window.location.href = newlang + newpathname;
}