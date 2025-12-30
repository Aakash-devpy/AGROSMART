document.addEventListener("DOMContentLoaded", () => {

    const enBtn = document.getElementById("en-btn");
    const hiBtn = document.getElementById("hi-btn");

    // If buttons are not present, do nothing
    if (!enBtn || !hiBtn) return;

    function switchLanguage(lang) {
        document.querySelectorAll("[data-en]").forEach(el => {
            el.textContent = el.dataset[lang];
        });

        enBtn.classList.toggle("active", lang === "en");
        hiBtn.classList.toggle("active", lang === "hi");

        localStorage.setItem("lang", lang);
    }

    // Button clicks
    enBtn.addEventListener("click", () => switchLanguage("en"));
    hiBtn.addEventListener("click", () => switchLanguage("hi"));

    // Restore saved language (default English)
    const savedLang = localStorage.getItem("lang") || "en";
    switchLanguage(savedLang);
});
