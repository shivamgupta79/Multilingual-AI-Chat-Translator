const socket = io();

document.getElementById("chatForm").addEventListener("submit", function (e) {
  e.preventDefault();
  const message = document.getElementById("message").value;
  const lang = document.getElementById("lang").value;
  socket.emit("chat_message", { message: message, target_lang: lang });
});

socket.on("translated_message", function (data) {
  const chatBox = document.getElementById("chatBox");
  if (data.error) {
    chatBox.innerHTML += `<p style="color:red;">Error: ${data.error}</p>`;
  } else {
    chatBox.innerHTML += `<p><b>${data.sender || "You"}:</b> ${data.original} → <i>${data.translated}</i> [${data.language}]</p>`;
  }
});
