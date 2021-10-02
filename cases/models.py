from django.db import models


class Claim(models.Model):
    CLAIM_TYPE = [
        ("rta", "RTA"),
        ("slip-trip", "Slip/Trip"),
        ("clinical-negligence", "Clinical Negligence"),
        ("works-accident", "Works Accident"),
        ("industrial-disease", "Industrial Disease"),
        ("hire-only", "Hire Only")
    ]

    CASE_STATUS = [
        ("just-started", "Just started"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
        ("dead-closed", "Dead/Closed")
    ]

    HANDLER = [
        ("claims-department", "Claims Department")
    ]

    claim_type = models.CharField(max_length=50, choices=CLAIM_TYPE)
    case_status = models.CharField(max_length=50, choices=CASE_STATUS)
    handler = models.CharField(max_length=50, choices=HANDLER)
    opened_date = models.DateTimeField(auto_now_add=True, verbose_name="File Opened Date")
    closed_date = models.DateTimeField(verbose_name="File Closed Date")
    opened_by = models.CharField(max_length=255, verbose_name="File Opened by")