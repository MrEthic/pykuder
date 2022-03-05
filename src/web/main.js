document.getElementById("next").addEventListener("click", ()=>{
  let a1 = parseInt(document.querySelector('input[class="r1"]:checked').value);
  let a2 = parseInt(document.querySelector('input[class="r2"]:checked').value);
  let a3 = parseInt(document.querySelector('input[class="r3"]:checked').value);
  if(a1 + a2 + a3 === 0 && a1 !== a2 && a1 !== a3 && a2 !== a3) {
    eel.next(a1, a2, a3);
  }
  else {
    alert('Verifiez vos réponses')
  }
}, false);

document.getElementById("prev").addEventListener("click", ()=>{
  eel.prev();
}, false);

eel.expose(update_with_stmt);
function update_with_stmt(s1, s2, s3, questionId, w1, w2, w3) {
  let pageId = Math.trunc(questionId / 10);
  document.getElementById("quId").innerHTML = `N°${questionId + 1}/134`;
  document.getElementById("pageId").innerHTML = `${pageId + 1}/14`;
  document.getElementById("s1").innerHTML = s1;
  document.getElementById("s2").innerHTML = s2;
  document.getElementById("s3").innerHTML = s3;

  for (let el of document.querySelectorAll('input[type="radio"]:checked')) {
    el.checked = false;
  }

  let select1 = `input[class="r1"][value="${w1}"]`;
  let select2 = `input[class="r2"][value="${w2}"]`;
  let select3 = `input[class="r3"][value="${w3}"]`;

  let a1 = document.querySelector(select1);
  let a2 = document.querySelector(select2);
  let a3 = document.querySelector(select3);

  if (a1 !== null) {
    a1.checked = true;
  }
  if (a2 !== null) {
    a2.checked = true;
  }
  if (a3 !== null) {
    a3.checked = true;
  }
}