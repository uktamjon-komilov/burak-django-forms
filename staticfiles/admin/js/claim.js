window.onload = () => {
    const username = document
        .getElementById("user-tools")
        .getElementsByTagName("strong")[0]
        .innerText.toLocaleLowerCase();

    const select = document.getElementById("id_opened_by");
    for (let i = 0; i < select.children.length; i++) {
        const option = select.children[i].innerText.toLocaleLowerCase();
        if (option == username) {
            select.options[i].selected = true;
        }
    }
}