window.onload = () => {
  const elemIsLicensed = document.getElementById("id_is_licensed");
  const elemLicensingAuth = document.querySelector(
    ".field-licensing_authority"
  );
  const elemSelAuth = document.getElementById("id_licensing_authority");

  if (elemIsLicensed.checked === true) {
    elemLicensingAuth.style.display = "block";
  } else {
    elemLicensingAuth.style.display = "none";
    for (var i = 0; i < elemSelAuth.options.length; i++) {
      elemSelAuth.options[i].selected = false;
    }
  }

  elemIsLicensed.addEventListener("click", () => {
    if (elemIsLicensed.checked === true) {
      elemLicensingAuth.style.display = "block";
    } else {
      elemLicensingAuth.style.display = "none";
      for (var i = 0; i < elemSelAuth.options.length; i++) {
        elemSelAuth.options[i].selected = false;
      }
    }
  });
};
