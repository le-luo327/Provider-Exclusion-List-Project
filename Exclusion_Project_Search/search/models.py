from django.db import models

class MainExclusions(models.Model):
    source_table = models.CharField(max_length=255)
    source_type = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    business_name = models.CharField(max_length=255)
    provider_type = models.CharField(max_length=255)
    npi = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255)
    exclusion_date = models.CharField(max_length=255)
    reinstatement_date = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'main_exclusions'