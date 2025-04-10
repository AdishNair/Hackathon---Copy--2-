document.getElementById("email-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const response = await fetch("/predict/email", {
        method: "POST",
        body: formData,
    });
    const result = await response.json();
    document.getElementById("email-result").innerText = "Result: " + result.result;
});

document.getElementById("url-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const response = await fetch("/predict/url", {
        method: "POST",
        body: formData,
    });
    const result = await response.json();
    document.getElementById("url-result").innerText = "Result: " + result.result;
});

document.getElementById("sender-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const response = await fetch("/predict/sender", {
        method: "POST",
        body: formData,
    });
    const result = await response.json();
    document.getElementById("sender-result").innerText = "Result: " + result.result;
});
