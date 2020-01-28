let flag = true;
let nTwoDots = 0;
let nTwoDotsLocal = 0;

function setCurrentCursorPosition(editor) {
    editor.setAttribute("contenteditable", "false");
    editor.setAttribute("contenteditable", "true");
};

setInterval(() => {
    const editor = document.getElementById("editor");

    let code = editor.innerText;
    let newCode;

    nTwoDots = code.split(":").length - 1;

    if (code.includes(":") && nTwoDots != nTwoDotsLocal) {
        let splitted = code.split(":");
        newCode = "";
        console.log(splitted);
        for (let i = 0; i < splitted.length; i++) {
            if (!i%2) newCode += "<span class='command'>" + splitted[i] + "</span>";
            else newCode += ":" + splitted[i] +"\n";
        }
        editor.innerHTML = newCode;
        setCurrentCursorPosition(editor);
        nTwoDotsLocal = splitted.length - 1;
    }



    // console.log(editor.innerHTML);

}, 1)

