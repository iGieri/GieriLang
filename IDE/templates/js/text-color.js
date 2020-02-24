let flag = false;
let nTwoDots = 0;
let nTwoDotsLocal = 0;
let newCode = "";

function setCurrentCursorPosition(editor) {
    editor.setAttribute("contenteditable", "false");
    editor.setAttribute("contenteditable", "true");
}

function print(string) {
    console.log(string);
}

setInterval(() => {
    const editor = document.getElementById("editor");

    let code = editor.innerText;

    nTwoDots = code.split(":").length - 1;

    let lines = code.split("\n");
    // print(lines);
    lines.forEach((line) => {
        if (line.includes(":") && nTwoDots !== nTwoDotsLocal) {
            let splitted = line.split(":");
            // newCode = "";
            print(splitted);
            for (let i = 0; i < splitted.length; i++) {
                if (!i%2) newCode += "<span class='command'>" + splitted[i] + "</span>";
                else newCode += ":" + splitted[i] + "\n";
            }
            flag = true;
            setCurrentCursorPosition(editor);
            nTwoDotsLocal = splitted.length - 1;
        }
    });

    if (flag) {
        editor.innerHTML = newCode;
        flag = false;
    }



    // console.log(newCode);

    // console.log(editor.innerHTML);

}, 1);

