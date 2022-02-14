from operator import truediv
from django.db import models

class Site(models.Model):
    siteName = models.CharField(max_length=200,null=True)
    siteAddress = models.TextField(null=True, blank=True)
    siteCity = models.CharField(max_length=200,null=True)
    siteOwner = models.CharField(max_length=200,null=True)
    siteOwnerNumber = models.BigIntegerField(null=True)
    siteVendor = models.CharField(max_length=200,null=True)
    siteProvider = models.CharField(max_length=200,null=True)
    siteFN = models.CharField(max_length=200,null=True)
    siteFiles = models.FileField(null=True, blank=True)
    sitKPIrepo = models.FileField(null=True, blank=True)
    siteDescription = models.TextField(null=True, blank=True)
    is4T6S = models.BooleanField(default=False)
    changedParts = models.TextField(null=True, blank=True)
    siteHistory = models.TextField(null=True, blank=True)
    siteLongitude  = models.CharField(max_length=200,null=True)
    siteLatitude = models.CharField(max_length=200,null=True)
    siteSFPType = models.CharField(max_length=200,null=True)
    freqis800 = models.BooleanField(default=False)
    freqIs2600F1 = models.BooleanField(default=False)
    freqIs2600F2 = models.BooleanField(default=False)
    siteType = models.CharField(max_length=200,null=True)
    siteTower = models.CharField(max_length=200,null=True)
    siteFiberLength = models.BigIntegerField(null=True)
    siteIP = models.CharField(max_length=200,null=True)
    siteCellId = models.JSONField(null=True)
    siteMaintenanceDates = models.JSONField(null=True)
    acceptanceDate = models.DateField('Acceptance',null=True)
    pub_date = models.DateTimeField('date published',null=True)

    def __str__(self):
        return self.siteName