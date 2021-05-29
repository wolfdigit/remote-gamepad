const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server, {
	cors: {
		origin: "*",
		methods: ["GET", "POST"],
	},
});

app.get('/', (req, res) => {
	  res.sendFile(__dirname + '/vgamepad.html');
});




io.on('connection', (socket) => {
	const sid = socket.id;
	let name = '';
	let prefix = `${sid}: `;
	console.log(prefix, 'a user connected');
	socket.on('identify', data => {
		name = data;
		prefix = `${sid}(${name}): `;
		console.log(prefix, 'identify');
	});
	socket.on('btn-control', (data) => {
		console.log(prefix, 'btn-control', data);
		io.emit('btn-control', data);
	});
});
io.on('disconnection', (socket) => {
	console.log(`${sid}: `, 'disconnected');
});



server.listen(3000, () => {
	  console.log('listening on *:3000');
});
