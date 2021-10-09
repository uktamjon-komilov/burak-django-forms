window.onload = () => {
  var vrmField = document.querySelector(".form-row.field-vehicle_dvla_number");
  vrmField.remove();

  const fieldsSet = document.querySelector(".module.aligned");
  const searchBox = `
<div class="form-row field-check_vehicle">
    <div style="display: flex; gap: 10px;">
        <label for="id_vehicle_dvla_number">Vehicle Registration Mark:</label>
        <input type="text" name="vehicle_dvla_number" value="" id="id_vehicle_dvla_number">
        <input type="button" value="Check" class="default" id="check_vehicle">
    </div>
</div>
`;

  const fieldHTML = fieldsSet.innerHTML;
  fieldsSet.innerHTML = searchBox + fieldHTML;

  var pathname = window.location.pathname;
  const vehicleId = pathname.split("/")[3];
  fetch("/fetch_dvla/vec/", {
    method: "POST",
    headers: {
      "Content-type": "application/json"
    },
    body: JSON.stringify({
      "vec": vehicleId
    })
  }).then(res => res.json())
  .then((data) => {
    document.getElementById("id_vehicle_dvla_number").value = data.value;
  })

  const checkBtn = document.getElementById("check_vehicle");
  const dvlaNumber = document.getElementById("id_vehicle_dvla_number");
  checkBtn.addEventListener("click", () => {
    number = dvlaNumber.value;
    console.log(number);
    fetchData(number);
  });

  const fetchData = (number) => {
    fetch("/fetch_dvla/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
      body: JSON.stringify({
        number: number,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        updateFields(data);
      });
  };

  const updateFields = (data) => {
    document.getElementById("id_color").value = data.colour;
    $(
      '#id_fuel_type option:contains("' + toTitleCase(data.fuelType) + '")'
    ).prop("selected", true);
    document.getElementById("id_make").value = data.make;
    document.getElementById("id_cc").value = data.engineCapacity;
    document.getElementById("id_mot_status").value = data.motStatus;
    document.getElementById("id_tax_expire_date").value = data.taxDueDate;
    document.getElementById("id_tax_status").value = data.taxStatus;
    document.getElementById("id_revenue_weight").value = data.revenueWeight;
    document.getElementById("id_type_approval").value = data.typeApproval;
    document.getElementById("id_wheel_plan").value = data.wheelplan;
    document.getElementById("id_last_v5c_issued").value =
      data.dateOfLastV5CIssued;
    document.getElementById("id_first_registration_date").value =
      data.monthOfFirstRegistration + "-01";
  };

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  function toTitleCase(str) {
    return str.replace(/\w\S*/g, function (txt) {
      return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
    });
  }

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

  const username = document
    .getElementById("user-tools")
    .getElementsByTagName("strong")[0]
    .innerText.toLocaleLowerCase();

  const select = document.getElementById("id_opened_by");
  for (let i = 0; i < select.children.length; i++) {
    const option = select.children[i].innerText.toLocaleLowerCase();
    if (option == username) {
      select.options[i].selected = true;
    }
  }

  const subCatDiv = document.querySelector(".form-row.field-sub_category");
  const miniSubCatDiv = document.querySelector(".form-row.field-inner_sub_category");
  console.log(subCatDiv);

  subCatDiv.children[0].innerHTML = `
    <label for="id_sub_category">Subcategory:</label>
    <select name="sub_category" id="id_sub_category">
      <option value="" selected="">---------</option>
    </select>
  `;
  miniSubCatDiv.children[0].innerHTML = `
    <label for="id_inner_sub_category">Inner subcategory:</label>
    <select name="inner_sub_category" id="id_inner_sub_category">
      <option value="" selected="">---------</option>
    </select>
  `;

  const cat = document.getElementById("id_category");
  const sub = document.getElementById("id_sub_category");
  const inner = document.getElementById("id_inner_sub_category");

  cat.addEventListener("change", () => {
    const catValue = cat.options[cat.selectedIndex].value;
    fetch("/fetch_dvla/sub/", {
      method: "POST",
      headers: {
        "Content-type": "application/json"
      },
      body: JSON.stringify({
        "cat": catValue
      })
    })
    .then(res => res.json())
    .then((data) => {
      sub.innerHTML = `<option value="" selected="">---------</option>`;
      data.forEach((item) => {
        sub.innerHTML += `<option value="${item}">${item}</option>`;
      });
    });
  });

  sub.addEventListener("change", () => {
    const catValue = cat.options[cat.selectedIndex].value;
    const subValue = sub.options[sub.selectedIndex].value;

    fetch("/fetch_dvla/mini/", {
      method: "POST",
      headers: {
        "Content-type": "application/json"
      },
      body: JSON.stringify({
        cat: catValue,
        sub: subValue,
      })
    })
    .then(res => res.json())
    .then((data) => {
      inner.innerHTML = `<option value="" selected="">---------</option>`;
      data.forEach((item) => {
        inner.innerHTML += `<option value="${item}">${item}</option>`;
      });
    })
  })
};
