document.getElementById("analyze-btn").addEventListener("click", async () => {
    const text = document.getElementById("text-input").value.trim();
    const apiKey = "ma_clé_secrète";

    if (!text) {
        alert("Veuillez entrer du texte !");
        return;
    }

    const response = await fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "x-api-key": apiKey
        },
        body: JSON.stringify({ text })
    });

    const resultDiv = document.getElementById("result");

    if (response.ok) {
        const data = await response.json();
        resultDiv.innerHTML = `<h3>Résultat :</h3>
                               <p><strong>Tokens:</strong> ${data.tokens.join(", ")}</p>
                               <p><strong>Leçons:</strong> ${data.lemmas.join(", ")}</p>
                               <p><strong>POS Tags:</strong> ${data.pos_tags.join(", ")}</p>`;
    } else {
        resultDiv.innerHTML = `<p style="color:red;">Erreur: ${response.statusText}</p>`;
    }
});