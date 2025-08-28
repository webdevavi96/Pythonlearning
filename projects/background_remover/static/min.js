const image = document.getElementById("img");
const text = document.getElementById("file-text");
const previewBox = document.querySelector(".preview-box");
const imgTag = document.querySelector(".imgBox");

image.addEventListener("change", () => {
  if (image.files.length > 0) {
    const file = image.files[0];
    text.textContent = "✅" + file.name;
    previewBox.style.display = "block";
    imgTag.src = URL.createObjectURL(file);
  } else {
    previewBox.style.display = "none";
    previewImg.src = "";
    text.textContent = "📁 Choose a file";
  }
});


