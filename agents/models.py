from django.db import models


class Agent(models.Model):
    TYPE = [
        ("referrer", "Referrer"),
        ("broker", "Broker"),
        ("engineer", "Engineer"),
        ("hire-company", "Hire Company"),
        ("panel-solicitor", "Panel Solicitor"),
        ("repairer", "Repairer")
    ]

    STATUS = [
        ("live", "Live"),
        ("dead", "Dead"),
        ("prospect", "Prospect")
    ]

    agent_type = models.CharField(max_length=50, choices=TYPE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    post_code = models.CharField(max_length=16)
    main_phone = models.CharField(max_length=20)
    contact_phone = models.CharField(max_length=16)
    fax = models.CharField(max_length=255)
    email = models.EmailField()
    status = models.CharField(max_length=50, choices=STATUS)

    
    def __str__(self):
        return "{} {}".format(self.name, self.agent_type)