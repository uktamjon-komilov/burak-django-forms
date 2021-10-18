from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Claim(models.Model):
    CLAIM_TYPE = [
        ("nrta", "Non Fault RTA"),
        ("rta", "Fault RTA"),
        # ("slip-trip", "Slip/Trip"),
        # ("clinical-negligence", "Clinical Negligence"),
        # ("works-accident", "Works Accident"),
        # ("industrial-disease", "Industrial Disease"),
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
    handler = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="handler")
    opened_date = models.DateTimeField(auto_now_add=True, verbose_name="File Opened Date")
    closed_date = models.DateTimeField(blank=True, verbose_name="File Closed Date")
    opened_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="File Opened by", related_name="opened_by")