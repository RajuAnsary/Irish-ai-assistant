const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");
const status = document.getElementById("status");
const wave = document.getElementById("wave");

setInterval(async () => {
  const res = await fetch("/status");
  const data = await res.json();
  status.textContent = data.status;
}, 1000);




startBtn.onclick = async () => {
  startBtn.disabled = true;
  stopBtn.disabled = false;
  status.textContent = "Starting Iris...";
  wave.classList.add("active");

  const res = await fetch("/start", { method: "POST" });
  const data = await res.json();

  status.textContent = data.status;
};


// STOP
stopBtn.onclick = async () => {
  await fetch("/stop", { method: "POST" });

  wave.classList.remove("active");
  status.textContent = "Idle";

  startBtn.disabled = false;
  stopBtn.disabled = true;
};
