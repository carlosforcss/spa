(() => {
    // Automatic process to deny google translation in icons
    let icons = document.getElementsByClassName("material-icons")
    for(let icon_idx = 0; icon_idx < icons.length; icon_idx += 1){
        const icon = icons[icon_idx]
        icon.classList.add("notranslate")
    }
})()