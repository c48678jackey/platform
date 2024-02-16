const express = require("express");

// 初始化
const app = express();

// 首頁 要傳送 地圖.html 給 user
app.get("/", (req, res) =>{
    res.sendFile( __dirname + "/" + "地圖.html");
});

// static files 像是 css, js, img, ... 之類的 靜態檔案 設定要去哪裡找
app.use(express.static( __dirname  ));  // 設定 規定好的 static file 資料夾去哪裡找

// socketIO 要做的事情
const http = require('http');
const server = http.createServer(app);
const socketIO = require('socket.io');
const io = socketIO(server);

// 把 socket 的事情 切分出去別的js處理
require("./app_socket_things")(io);

// 本來是用 app.listen, 但為了用 socketIO, 改用 http_server.listen喔～
server.listen(3000, () => {
    console.log("Server on port 3000");
});
