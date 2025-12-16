let encryptedData = "";
let signatureData = "";

function encrypt() {
    fetch("/encrypt", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ text: inputText.value })
    })
    .then(res => res.json())
    .then(data => {
        encryptedData = data.result;
        result.textContent = "AES-256 ENCRYPTED:\n" + data.result;
    });
}

function decrypt() {
    fetch("/decrypt", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ text: encryptedData })
    })
    .then(res => res.json())
    .then(data => {
        result.textContent = "DECRYPTED TEXT:\n" + data.result;
    });
}

function hash() {
    fetch("/hash", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ text: inputText.value })
    })
    .then(res => res.json())
    .then(data => {
        result.textContent = "SHA-256 HASH:\n" + data.result;
    });
}

function sign() {
    fetch("/sign", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ text: inputText.value })
    })
    .then(res => res.json())
    .then(data => {
        signatureData = data.result;
        result.textContent = "RSA SIGNATURE:\n" + data.result;
    });
}

function verify() {
    fetch("/verify", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            text: inputText.value,
            signature: signatureData
        })
    })
    .then(res => res.json())
    .then(data => {
        result.textContent = "RSA VERIFICATION RESULT:\n" + data.result;
    });
}

function tls() {
    fetch("/tls")
    .then(res => res.json())
    .then(data => {
        result.textContent =
            "TLS VERSION: " + data.protocol + "\n" +
            "CIPHER SUITE: " + data.cipher;
    });
}
