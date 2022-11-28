from django.db import models


class Tasks(models.Model):
    EQUIPMENTS = [
        ("GREEN", "Green"),
        ("BLUE", "Blue"),
        ("AURORA", "Aurora"),
        ("THERMAL", "Thermal"),
    ]

    company_name = models.CharField(max_length=255)
    plates = models.CharField(max_length=25)
    file_name = models.CharField(max_length=255)
    which_equipment = models.CharField(max_length=50, choices=EQUIPMENTS)
    date_added = models.DateField(auto_now_add=True)
    time_added = models.TimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    on_ready = models.BooleanField(default=False)
    all_info = models.CharField(max_length=555)

    def __str__(self):
        return self.company_name, self.plates, self.file_name


