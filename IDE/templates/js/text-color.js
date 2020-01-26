setInterval(() => {
    const editor = document.getElementById("editor");

    let code = editor.innerHTML;
    let newCode;

    if (code.includes("print")) {
        let splitted = code.split("print");
        newCode = splitted[0] + "<span class='print'>print</span>" + splitted[1];
        editor.innerHTML = newCode;
    }

    console.log(editor.innerHTML);

}, 1)