let flag = true;

setInterval(() => {
    const editor = document.getElementById("editor");

    let code = editor.innerText;
    let newCode;

    if (code.includes("print") && flag) {
        let splitted = code.split("print");
        newCode = splitted[1] + "<span class='print'>print</span>" + splitted[0];
        editor.innerHTML = newCode;
        flag = false;
    }

    console.log(editor.innerHTML);

}, 1)