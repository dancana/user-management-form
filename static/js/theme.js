document.addEventListener("DOMContentLoaded", () => {
  const toggleBtn = document.getElementById("theme-toggle");

  toggleBtn.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");

    // Save theme to localStorage
    if (document.body.classList.contains("dark-mode")) {
      localStorage.setItem("theme", "dark");
    } else {
      localStorage.setItem("theme", "light");
    }
  });

  // Load theme from storage
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme === "dark") {
    document.body.classList.add("dark-mode");
  }
});
