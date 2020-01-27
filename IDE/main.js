const electron = require("electron");
const { app, BrowserWindow } = require('electron');

function createWindow() {
    let win = new BrowserWindow({
        // titleBarStyle: "hidden",
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true
        }
        // icon: path.join(__dirname, "img/logo.png")
    });

  -
      win.loadFile('templates/index.html');
}

app.on("ready", createWindow);

