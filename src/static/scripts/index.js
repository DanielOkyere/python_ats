/**
 * Toggle Menu for hamburger
 */

function toggleMenu() {
    let icon = document.getElementById("nav__items");
    console.log(icon);

    if (icon.classList.contains("show_menu")) {
        icon.classList.remove("show_menu");
        icon.classList.add("hide_menu");
    } else if(icon.classList.contains('hide_menu')) {
        icon.classList.remove("hide_menu");
        icon.classList.add("show_menu");
    } else {
        icon.classList.add('show_menu');
    }
}
