window.onload = () => {
  const fieldsSet = document.querySelector(".module.aligned");
  const searchBox = `
<div class="form-row field-check_vehicle">
    <div style="display: flex; gap: 10px;">
        <label for="vehicle_dvla_number">Vehicle Registration Mark:</label>
        <input type="text" value="" id="vehicle_dvla_number">
        <input type="button" value="Check" class="default" id="check_vehicle">
    </div>
</div>
`;

  const fieldHTML = fieldsSet.innerHTML;
  fieldsSet.innerHTML = searchBox + fieldHTML;

  const checkBtn = document.getElementById("check_vehicle");
  const dvlaNumber = document.getElementById("vehicle_dvla_number");
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

  const categorySelect = document.getElementById("id_category");
  const subCategorySelect = document.getElementById("id_sub_category");

  for (let i = 0; i < subCategorySelect.children.length; i++) {
    if (i > 7) {
      subCategorySelect.children[i].style.display = "none";
      console.log(subCategorySelect.children[i]);
    }
  }

  categorySelect.addEventListener("change", () => {
    if (categorySelect.options[categorySelect.selectedIndex].value == "cars") {
      for (let i = 0; i < subCategorySelect.children.length; i++) {
        if (i > 7) {
          console.log(subCategorySelect.children[i]);
          subCategorySelect.children[i].style.display = "unset";
        }
      }
    } else {
      for (let i = 0; i < subCategorySelect.children.length; i++) {
        if (i > 7) {
          subCategorySelect.children[i].style.display = "none";
        }
      }
    }
  });
};
