function lang_home() {
    var pathname = window.location.pathname.split('/');
    if (pathname[1] == "en" || pathname[1] == "ko"){
        window.location.href = "/" + pathname[1] + "/";
    }
    else {
        window.location.href = "/";
    }
}

function lang_select() {
    var pathname = window.location.pathname.split('/');
    
    if (pathname[1] !== "en" && pathname[1] !== "ko") {
        return;  // 언어 경로가 아니면 아무것도 하지 않음
    }
    
    var newlang = pathname[1] === "en" ? "/ko" : "/en";
    var newpathname = "";
    
    for (var i = 2; i < pathname.length; i++) {
        newpathname += "/";
        newpathname += pathname[i];
    }
    window.location.href = newlang + newpathname;
}