const dropZone = document.getElementById("drop-zone");
const fileInput = document.getElementById("leaf_image");
const previewWrapper = document.getElementById("preview-wrapper");
const imgPreview = document.getElementById("img-preview");
const removeBtn = document.getElementById("remove-img");
const overlay = document.getElementById("drag-overlay");

let dragCounter = 0;

/* CLICK UPLOAD */
dropZone.addEventListener("click", () => fileInput.click());

/* FILE SELECT */
fileInput.addEventListener("change", () => {
  if (fileInput.files[0]) showPreview(fileInput.files[0]);
});

/* DRAG OVERLAY FIX */
document.addEventListener("dragenter", e => {
  e.preventDefault();
  dragCounter++;
  overlay.classList.add("active");
});

document.addEventListener("dragleave", e => {
  dragCounter--;
  if (dragCounter === 0) overlay.classList.remove("active");
});

document.addEventListener("dragover", e => e.preventDefault());

document.addEventListener("drop", e => {
  e.preventDefault();
  overlay.classList.remove("active");
  dragCounter = 0;

  if (e.dataTransfer.files.length) {
    fileInput.files = e.dataTransfer.files;
    showPreview(e.dataTransfer.files[0]);
  }
});

/* PREVIEW */
function showPreview(file) {
  imgPreview.src = URL.createObjectURL(file);
  previewWrapper.classList.remove("hidden");
  document.getElementById("drop-text").style.display = "none";
}

removeBtn.addEventListener("click", e => {
  e.stopPropagation();
  fileInput.value = "";
  previewWrapper.classList.add("hidden");
  document.getElementById("drop-text").style.display = "block";
});
/* LANGUAGE TOGGLE */
const enBtn = document.getElementById("en-btn");
const hiBtn = document.getElementById("hi-btn");

function switchLanguage(lang) {
  document.querySelectorAll("[data-en]").forEach(el => {
    el.textContent = el.dataset[lang];
  });

  enBtn.classList.toggle("active", lang === "en");
  hiBtn.classList.toggle("active", lang === "hi");
}

enBtn.addEventListener("click", () => switchLanguage("en"));
hiBtn.addEventListener("click", () => switchLanguage("hi"));
