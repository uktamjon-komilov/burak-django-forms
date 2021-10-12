from django.db import models
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField

from .category import CATEGORY


User = get_user_model()


class LicensingAuthority(models.Model):
    name = models.CharField(null=True, blank=True, max_length=255, verbose_name="Licensing Authority")
    address = models.TextField(null=True, blank=True)
    postcode = models.CharField(null=True, blank=True, max_length=20)
    tel_main = models.CharField(null=True, blank=True, max_length=20)
    tel_contact = models.CharField(null=True, blank=True, max_length=20)
    fax = models.CharField(null=True, blank=True, max_length=20)
    email_main = models.CharField(null=True, blank=True, max_length=128, verbose_name="E-mail main")
    contact_name = models.CharField(null=True, blank=True, max_length=128)

    miscellaneous_notes = models.TextField(null=True, blank=True, verbose_name="Miscellaneous Notes")
    date_file_opened = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    date_file_closed = models.DateTimeField(null=True, blank=True)
    opened_by = models.CharField(null=True, blank=True, max_length=128)


    def __str__(self):
        return "{}, {}, {}".format(self.name, self.postcode, self.tel_main)


class Hire(models.Model):
    claims_case_reference = models.CharField(null=True, blank=True, max_length=128)
    claim_type = models.CharField(null=True, blank=True, max_length=128)
    client_name = models.CharField(null=True, blank=True, max_length=128)
    address = models.TextField(null=True, blank=True)
    postcode = models.CharField(null=True, blank=True, max_length=128)
    tel_main = models.CharField(null=True, blank=True, max_length=128)
    hire_vehicle_out_date = models.DateTimeField(null=True, blank=True)
    hire_vehicle_back_date = models.DateTimeField(null=True, blank=True)

    reserved = models.BooleanField(null=True, blank=True)
    claims_case_reference_2 = models.CharField(null=True, blank=True, max_length=128, verbose_name="Claims case reference")
    username = models.CharField(null=True, blank=True, max_length=128)
    date_reserved = models.DateTimeField(null=True, blank=True)


class Service(models.Model):
    SERVICE_TYPE = [
        ("servicing", "Servicing"),
        ("oil", "Oil"),
        ("professional-valet", "Professional Valet"),
        ("miscellenaous", "Miscellenaous"),
        ("tyres", "Tyres"),
        ("windscreen", "Windscreen"),
        ("body-work-repairs", "Body Work Repairs"),
        ("mechanical-repair", "Mechanical Repairs"),
        ("wiper-blades", "Wiper Blades"),
        ("bulb-replacement", "Bulb replacement"),
        ("keys", "Keys"),
    ]

    last_mot = models.DateTimeField(null=True, blank=True)
    next_mot_due = models.DateTimeField(null=True, blank=True)

    last_service = models.DateTimeField(null=True, blank=True)
    last_service_miles = models.FloatField(null=True, default=0.0, help_text="in miles")
    next_service_due = models.DateTimeField(null=True, blank=True)
    next_service_due_miles = models.FloatField(default=0.0, help_text="in miles")

    next_service_due_in = models.FloatField(default=0.0)

    vehicle_cost_to_date = models.FloatField(default=0.0, help_text="in £. Note: All servicing, repair and misc vehicle costs should be entered using this screen. Entries can be added with a Zero cost if necessary to maintain a detailed summary.")

    date = models.DateTimeField(null=True, blank=True)
    service_type = models.CharField(max_length=50, null=True, blank=True, choices=SERVICE_TYPE, verbose_name="Type")
    invoice_no = models.CharField(max_length=128, null=True, blank=True, help_text="If applicable")
    vat = models.FloatField(default=0.0, help_text="in £", null=True, blank=True)

    amount = models.FloatField(default=0.0, help_text="in £")
    supplier_name = models.CharField(null=True, blank=True, max_length=128, help_text="Garage, shop etc.")
    misc_details = models.TextField(null=True, blank=True, help_text="20K service. Rear Indicator Bulb replacement")

    last_recorded_mileage = models.FloatField(null=True, blank=True)
    as_at = models.DateField(verbose_name="", null=True, blank=True)


class Supplier(models.Model):
    name = models.CharField(null=True, blank=True, max_length=255)
    address = models.TextField(null=True, blank=True)
    postcode = models.CharField(null=True, blank=True, max_length=255)
    telephone = models.CharField(null=True, blank=True, max_length=255)
    fax = models.CharField(null=True, blank=True, max_length=255)
    contact_name = models.CharField(null=True, blank=True, max_length=255)
    tel_contact = models.CharField(null=True, blank=True, max_length=255)
    
    purchase_price = models.FloatField(null=True, blank=True, help_text="in £")
    purchase_price_vat = models.FloatField(null=True, blank=True, help_text="in £", verbose_name="Purchase price VAT")
    purchase_date = models.DateTimeField(null=True, blank=True)
    first_registration_date = models.DateTimeField(null=True, blank=True)


class Finance(models.Model):
    name = models.CharField(null=True, blank=True, max_length=255)
    address = models.TextField(null=True, blank=True)
    postcode = models.CharField(null=True, blank=True, max_length=255)
    telephone = models.CharField(null=True, blank=True, max_length=255)
    fax = models.CharField(null=True, blank=True, max_length=255)
    contact_name = models.CharField(null=True, blank=True, max_length=255)
    tel_contact = models.CharField(null=True, blank=True, max_length=255)
    
    purchase_price = models.FloatField(null=True, blank=True, help_text="in £")
    purchase_price_vat = models.FloatField(null=True, blank=True, help_text="in £", verbose_name="Purchase price VAT")
    purchase_date = models.DateTimeField(null=True, blank=True)
    first_registration_date = models.DateTimeField(null=True, blank=True)
    agreement_no = models.CharField(null=True, blank=True, max_length=255)
    length_of_agreement = models.IntegerField(null=True, blank=True, help_text="Mths")
    lease_return_date = models.DateTimeField(null=True, blank=True)
    lease_return_miles = models.FloatField(null=True, blank=True)
    lease_miles_remaining = models.FloatField(null=True, blank=True)


class Sale(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    forename = models.CharField(null=True, blank=True, max_length=255)
    surname_or_company = models.CharField(null=True, blank=True, max_length=255, verbose_name="Surname/Company")
    address = models.TextField(null=True, blank=True)
    postcode = models.CharField(null=True, blank=True, max_length=255)
    telephone = models.CharField(null=True, blank=True, max_length=255)
    fax = models.CharField(null=True, blank=True, max_length=255)
    contact_name = models.CharField(null=True, blank=True, max_length=255)
    tel_contact = models.CharField(null=True, blank=True, max_length=255)
    
    date_sold = models.DateTimeField(null=True, blank=True)
    mileage = models.FloatField(null=True, blank=True)
    guid_price = models.FloatField(null=True, blank=True, help_text="in £")
    sale_price = models.FloatField(null=True, blank=True, help_text="in £")


class Vehicle(models.Model):
    VEHICLE_STATUS = [
        ("available", "Available"),
        ("on-hire", "On hire"),
        ("off-fleet", "Off Fleet"),
        ("in-repair", "In Repair"),
        ("in-for-service", "In for Service"),
    ]

    VEHICLE_CATEGORY = [
        (cat, cat) for cat in CATEGORY.keys()
    ]

    VEHICLE_DEPOT = [
        ("all-depots", "All depots"),
        ("depot-1", "Depot 1"),
        ("depot-2", "Depot 2"),
        ("571-cable-street", "571 Cable Street"),
        ("cross-hire", "Cross Hire"),
    ]

    FUEL_TYPE = [
        ("diesel", "Diesel"),
        ("lpg", "LPG"),
        ("petrol", "Petrol"),
        ("hybrid-electric", "Hybrid Electric"),
        ("plug-in-hybrid", "Plug-In Hybrid"),
        ("electricity", "Electricity"),
    ]

    INS_COVER = ((True, "Yes"), (False, "No"))

    TRANSMISSION = [
        ("automatic", "AUTOMATIC"),
        ("manual", "MANUAL")
    ]


    vehicle_dvla_number = models.CharField(max_length=255, null=True, blank=True)
    cross_hire = models.BooleanField()
    vehicle_status = models.CharField(max_length=50, choices=VEHICLE_STATUS)
    currently_reserved = models.BooleanField(verbose_name="Is vehicle currently reserved?")
    opened_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    category = models.CharField(max_length=255, blank=True, null=True, choices=VEHICLE_CATEGORY, verbose_name="Vehicle category")
    sub_category = models.CharField(max_length=255, blank=True, null=True, verbose_name="Vehicle Type Category")
    inner_sub_category = models.CharField(max_length=255, blank=True, null=True, verbose_name="GTA Group Category")
    depot = models.CharField(max_length=25, choices=VEHICLE_DEPOT, verbose_name="Depot/Branch", help_text="eg. DE51 BBY")
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255, verbose_name="Colour")
    cc = models.CharField(max_length=255, verbose_name="CC")
    mot_status = models.CharField(max_length=255, default="")
    revenue_weight = models.CharField(max_length=255, default="", blank=True)
    type_approval = models.CharField(max_length=255, default="", blank=True)
    radio_code = models.CharField(max_length=255, null=True, blank=True)
    vin = models.CharField(max_length=255, verbose_name="VIN", null=True, blank=True)
    number_of_doors = models.IntegerField(null=True, blank=True)
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPE)
    first_registration_date = models.DateField(null=True, blank=True)
    tax_expire_date = models.DateField(null=True, blank=True)
    tax_status = models.CharField(max_length=255, null=True, blank=True)
    last_v5c_issued = models.DateField(null=True, blank=True)
    wheel_plan = models.CharField(max_length=255, null=True, blank=True)

    insurance_cover = models.BooleanField(default=False, choices=INS_COVER)
    insurance_group = models.CharField(max_length=255, null=True, blank=True)

    transmission = MultiSelectField(choices=TRANSMISSION)

    is_licensed = models.BooleanField()
    licensing_authority = models.ManyToManyField(LicensingAuthority, blank=True, related_name="vehicle")

    hire_details = models.OneToOneField(Hire, on_delete=models.SET_NULL, null=True, related_name="vehicle")
    service_details = models.OneToOneField(Service, on_delete=models.SET_NULL, null=True, related_name="vehicle")
    supplier_details = models.OneToOneField(Supplier, on_delete=models.SET_NULL, null=True, related_name="vehicle")
    finance_details = models.OneToOneField(Finance, on_delete=models.SET_NULL, null=True, related_name="vehicle")
    sale_details = models.OneToOneField(Sale, on_delete=models.SET_NULL, null=True, related_name="vehicle")


    def save(self, *args, **kwargs):
        if self.id is None:
            hire = Hire.objects.create()
            self.hire_details = hire

            service = Service.objects.create()
            self.service_details = service

            supplier = Supplier.objects.create()
            self.supplier_details = supplier

            finance = Finance.objects.create()
            self.finance_details = finance

            sale = Sale.objects.create()
            self.sale_details = sale        

        super(Vehicle, self).save(*args, **kwargs)
        if not self.is_licensed:
            self.licensing_authority.clear()
        super(Vehicle, self).save(*args, **kwargs)
    

    @property
    def own_link(self):
        return "/vehicles/vehicle/{}/change/".format(self.id)

    @property
    def hire_link(self):
        return "/vehicles/hire/{}/change/".format(self.hire_details.id)

    @property
    def service_link(self):
        return "/vehicles/service/{}/change/".format(self.service_details.id)

    @property
    def supplier_link(self):
        return "/vehicles/supplier/{}/change/".format(self.supplier_details.id)

    @property
    def finance_link(self):
        return "/vehicles/finance/{}/change/".format(self.finance_details.id)

    @property
    def sale_link(self):
        return "/vehicles/sale/{}/change/".format(self.sale_details.id)