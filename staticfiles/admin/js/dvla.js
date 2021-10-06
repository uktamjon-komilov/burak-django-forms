window.onload = () => {
  const fieldsSet = document.querySelector(".module.aligned");
  const searchBox = `
<div class="form-row field-check_vehicle">
    <div style="display: flex; gap: 10px;">
        <label for="vehicle_dvla_number">VES Number:</label>
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
};
