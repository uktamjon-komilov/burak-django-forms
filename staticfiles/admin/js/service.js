window.onload = () => {
  const dateField = document.getElementById("id_as_at");
  const asAt = document.querySelector(".form-row.field-as_at");
  const shortcuts = asAt.querySelector(".datetimeshortcuts");

  const lastMileage = document.querySelector(
    "#service_form > div > fieldset > div.form-row.field-last_recorded_mileage > div"
  );

  lastMileage.append(dateField);
  lastMileage.append(shortcuts);

  asAt.style.display = "none";
};
