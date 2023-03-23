
const uploadBtn = document.querySelector("#uploadBtn")
const fileField = document.querySelector("#formFileLg")
uploadBtn.addEventListener("click", uploadFile)
fileField.addEventListener("change", changeVisibility)


async function uploadFile(event) {
    const formData = new FormData()
    event.preventDefault()
    formData.append('file', fileField.files[0])
    const statusDiv = document.getElementById("status")
    statusDiv.innerText = "Файл обрабатывается..."
    uploadBtn.classList.add('d-none')
    const response = await fetch("/", { method: "POST", body: formData });
    const data = await response.json()
    console.log('Успех:', JSON.stringify(data));
    statusDiv.innerText = ""
    const resultText = document.getElementById("resultText")
    const textParagraph = document.createElement("p")
    textParagraph.innerText = data['text']
    resultText.insertAdjacentElement("afterbegin", textParagraph)
}

async function changeVisibility(event) {
    uploadBtn.classList.remove('d-none')
    resultText.innerText = ""
}