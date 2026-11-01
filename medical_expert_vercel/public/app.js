// Runs only on the symptom entry page.
(function () {
  const form = document.getElementById("checkForm");
  if (!form) return;

  const boxes = Array.from(form.querySelectorAll('input[name="symptoms"]'));
  const chips = Array.from(form.querySelectorAll(".chip"));
  const countEl = document.getElementById("count");
  const searchEl = document.getElementById("symSearch");
  const textEl = document.getElementById("symText");
  const clearBtn = document.getElementById("clearBtn");
  const micBtn = document.getElementById("micBtn");

  // Highlight selected chips and update the counter
  function refresh() {
    let n = 0;
    boxes.forEach((box) => {
      box.parentElement.classList.toggle("on", box.checked);
      if (box.checked) n += 1;
    });
    countEl.textContent = n;
  }
  boxes.forEach((box) => box.addEventListener("change", refresh));

  // Search box filters the chips (works with names in any language)
  searchEl.addEventListener("input", () => {
    const q = searchEl.value.trim().toLowerCase();
    chips.forEach((chip) => {
      const hay = (chip.dataset.search || "") + " " + chip.textContent.toLowerCase();
      chip.classList.toggle("hidden", q !== "" && !hay.includes(q));
    });
  });

  // Clear everything
  clearBtn.addEventListener("click", () => {
    boxes.forEach((box) => (box.checked = false));
    textEl.value = "";
    searchEl.value = "";
    chips.forEach((chip) => chip.classList.remove("hidden"));
    refresh();
  });

  // Voice input (Chrome / Edge). Hidden when the browser has no support.
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (SR && micBtn) {
    micBtn.hidden = false;
    const label = micBtn.querySelector("span");
    const idleText = label.textContent;
    let rec = null;

    micBtn.addEventListener("click", () => {
      if (rec) {
        rec.stop();
        return;
      }
      rec = new SR();
      rec.lang = form.dataset.speech || "en-IN";
      rec.interimResults = false;
      rec.maxAlternatives = 1;

      micBtn.classList.add("listening");
      label.textContent = form.dataset.listening || "...";

      rec.onresult = (event) => {
        const said = event.results[0][0].transcript.trim();
        if (said) {
          textEl.value = textEl.value.trim()
            ? textEl.value.trim() + ", " + said
            : said;
        }
      };
      const done = () => {
        micBtn.classList.remove("listening");
        label.textContent = idleText;
        rec = null;
      };
      rec.onend = done;
      rec.onerror = done;
      rec.start();
    });
  }

  refresh();
})();
