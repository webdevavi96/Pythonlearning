function addValue(val) {
  let exp = document.querySelector("#input-box");

  if (val === "") exp.value = "";
  else if (exp.value === "0") exp.value = val;
  else exp.value += val;
}
