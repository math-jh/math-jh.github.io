function darkmode(){
    var defaultTheme = [...document.styleSheets].find(style => /(main.css)$/.test(style.href))
    var darkTheme = [...document.styleSheets].find(style => /(main_dark.css)$/.test(style.href))

    if (darkTheme) {
        const darkModeCookie = document.cookie
            .split('; ')
            .find(co => co.startsWith('MDARK='))
        if (darkModeCookie !== undefined) {
            const dmodeValue = darkModeCookie.split('=')[1]
            darkTheme.disabled = dmodeValue !== 'Y'
            defaultTheme.disabled = dmodeValue === 'Y'
        } else {
            if (matchMedia('(prefers-color-scheme: dark)').matches) {
                darkTheme.disabled = false
                defaultTheme.disabled = true
            } else {
                darkTheme.disabled = true
                defaultTheme.disabled = false
            }
            document.cookie = `MDARK=${darkTheme.disabled ? 'N' : 'Y'}; path=/;`
        }

        let toggleThemeBtn = document.getElementById("toggle_dark_theme")
        if (toggleThemeBtn) {
            toggleThemeBtn.checked = defaultTheme.disabled
        }

        let changeTheme = () => {
            darkTheme.disabled = !darkTheme.disabled
            defaultTheme.disabled = !darkTheme.disabled
            document.cookie = `MDARK=${darkTheme.disabled ? 'N' : 'Y'}; path=/;`
        }

        toggleThemeBtn.addEventListener('click', changeTheme)
    }
}

function scrollbar() {
if(document.getElementById("toggle_dark_theme").checked == true)
document.head.querySelector("#scrollbar-color").innerHTML=`
   body::-webkit-scrollbar-thumb {background-color:#455a64; border-radius: 3px; background-clip: padding-box; border:2px solid transparent}
   .sidebar.sticky::-webkit-scrollbar-thumb {background-color:#282828; border-radius: 3px; background-clip: padding-box; border:1px solid transparent}
   .toc__menu::-webkit-scrollbar-thumb {background-color:#282828; border-radius: 3px; background-clip: padding-box; border:1px solid transparent}
 `
 else
 document.head.querySelector("#scrollbar-color").innerHTML=`
   body::-webkit-scrollbar-thumb {background-color:#cfd8dc; border-radius: 3px; background-clip: padding-box; border:2px solid transparent}
   .sidebar.sticky::-webkit-scrollbar-thumb {background-color:#eaeaf2; border-radius: 3px; background-clip: padding-box; border:1px solid transparent}
   .toc__menu::-webkit-scrollbar-thumb {background-color:#eaeaf2; border-radius: 3px; background-clip: padding-box; border:1px solid transparent}
 `
 }