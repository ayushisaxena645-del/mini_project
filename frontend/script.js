
document.getElementById("analysisForm").addEventListener("submit", async function(event) {

    event.preventDefault();

    const url = document.getElementById("urlInput").value.trim();
    const resultBox = document.getElementById("result");

    resultBox.innerText = "Analyzing URL...";

    try {
        const response = await fetch("/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: url })
        });

        const result = await response.json();

        if (!response.ok) {
            resultBox.innerText = result.error || "Something went wrong.";
            return;
        }

        resultBox.innerText =
            result.message + (result.domain ? " | Domain: " + result.domain : "");

    } catch (error) {
        resultBox.innerText = "Unable to connect to Flask server.";
    }
});
