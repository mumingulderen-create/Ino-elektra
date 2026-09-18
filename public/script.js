const CONFIG = {
  phone: "+31628763775",
  whatsapp: "31628763775",
  email: "info@ino-elektra.nl"
};

document.getElementById("menuBtn")?.addEventListener("click", () => {
  document.getElementById("nav")?.classList.toggle("open");
});
document.querySelectorAll("#nav a").forEach(a => a.addEventListener("click", () => document.getElementById("nav")?.classList.remove("open")));

const photoInput = document.getElementById("photos");
const photoList = document.getElementById("photoList");
if (photoInput && photoList) {
  photoInput.addEventListener("change", () => {
    const files = [...photoInput.files];
    photoList.textContent = files.length ? `${files.length} bestand(en) geselecteerd: ${files.map(f => f.name).join(", ")}` : "";
  });
}

document.querySelectorAll(".faq-q").forEach(btn => {
  btn.addEventListener("click", () => {
    const answer = btn.nextElementSibling;
    answer?.classList.toggle("open");
    const span = btn.querySelector("span");
    if (span && answer) {
      span.textContent = answer.classList.contains("open") ? "−" : "+";
    }
  });
});

const mapEnlargeBtn = document.getElementById("mapEnlargeBtn");
const mapModal = document.getElementById("mapModal");
const mapModalClose = document.getElementById("mapModalClose");
if (mapEnlargeBtn && mapModal) {
  mapEnlargeBtn.addEventListener("click", () => mapModal.classList.add("open"));
  mapModalClose?.addEventListener("click", () => mapModal.classList.remove("open"));
  mapModal.addEventListener("click", (e) => { if (e.target === mapModal) mapModal.classList.remove("open"); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") mapModal.classList.remove("open"); });
}

const dateInput = document.getElementById("date");
if (dateInput) dateInput.min = new Date().toISOString().split("T")[0];

function wireAjaxForm(form, { successMsg = "Je aanvraag is verzonden naar INO. We nemen zo snel mogelijk contact met je op.", resetPhotoList = false } = {}) {
  if (!form) return;
  const submitBtn = form.querySelector("button[type='submit']");
  const originalLabel = submitBtn ? submitBtn.textContent : "Versturen";
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const name = data.get("name") || "";
    const result = form.querySelector("#formResult") || document.getElementById("formResult");

    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.textContent = "Versturen...";
    }
    if (result) result.hidden = true;

    try {
      const response = await fetch("https://formsubmit.co/ajax/info@ino-elektra.nl", {
        method: "POST",
        body: data,
        headers: { "Accept": "application/json" }
      });
      if (!response.ok) throw new Error("Verzenden mislukt");

      if (result) {
        result.hidden = false;
        result.className = "form-result";
        result.innerHTML = `<strong>Aanvraag verstuurd.</strong><br>Bedankt ${escapeHtml(name)}, ${successMsg}`;
        result.scrollIntoView({behavior:"smooth", block:"center"});
      }
      form.reset();
      if (resetPhotoList) {
        const photoList = document.getElementById("photoList");
        if (photoList) photoList.textContent = "";
      }
    } catch (err) {
      if (result) {
        result.hidden = false;
        result.className = "form-result form-result-error";
        result.innerHTML = `<strong>Er ging iets mis.</strong><br>Je aanvraag kon niet worden verzonden. Bel ons gerust direct op <a href="tel:+31628763775">06 28 76 37 75</a> of probeer het opnieuw.`;
        result.scrollIntoView({behavior:"smooth", block:"center"});
      } else {
        alert("Er ging iets mis bij het verzenden. Bel ons gerust direct op 06 28 76 37 75.");
      }
    } finally {
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.textContent = originalLabel;
      }
    }
  });
}

wireAjaxForm(document.getElementById("quoteForm"), { resetPhotoList: true });
wireAjaxForm(document.getElementById("spoedForm"), { successMsg: "we bellen je zo snel mogelijk terug." });

const appointmentForm = document.getElementById("appointmentForm");
if (appointmentForm) {
  appointmentForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const form = e.currentTarget;
    const data = new FormData(form);
    const submitBtn = form.querySelector("button[type='submit']");

    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.textContent = "Versturen...";
    }

    try {
      const response = await fetch("https://formsubmit.co/ajax/info@ino-elektra.nl", {
        method: "POST",
        body: data,
        headers: { "Accept": "application/json" }
      });
      if (!response.ok) throw new Error("Verzenden mislukt");
      alert("Je voorkeur is verstuurd naar INO. We bevestigen de afspraak persoonlijk.");
      form.reset();
    } catch (err) {
      alert("Je voorkeur kon niet worden verstuurd. Bel ons gerust direct op 06 28 76 37 75.");
    } finally {
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.textContent = "Voorkeur aanvragen";
      }
    }
  });
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[c]));
}

