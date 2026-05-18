async function sendText() {
    const text = document.getElementById("inputText").value;

    const response = await fetch("http://127.0.0.1:5000/process", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text })
    });

    const data = await response.json();

    document.getElementById("output").textContent =
        JSON.stringify(data, null, 2);
}