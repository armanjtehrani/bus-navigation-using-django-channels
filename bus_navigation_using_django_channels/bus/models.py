from django.db import models


class Line(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Station(models.Model):
    name = models.CharField(max_length=100)
    line = models.ForeignKey(Line, related_name='stations', on_delete=models.CASCADE)
    next_station = models.ForeignKey('self', related_name='my_prev_station', on_delete=models.SET_NULL, null=True, blank=True)
    prev_station = models.ForeignKey('self', related_name='my_next_station', on_delete=models.SET_NULL, null=True, blank=True)
    is_final_station = models.BooleanField(default=False)
    bus_wait_time = models.IntegerField(default=5)
    x_pos = models.FloatField()
    y_pos = models.FloatField()

    def __str__(self):
        return self.name


class Bus(models.Model):
    line = models.ForeignKey(Line, related_name='buses', on_delete=models.SET_NULL, null=True, blank=True)
    speed = models.FloatField(default=0.000535)
    x_pos = models.FloatField()
    y_pos = models.FloatField()
    prev_station = models.ForeignKey(Station, related_name='next_buses', on_delete=models.SET_NULL, null=True, blank=True)
    next_station = models.ForeignKey(Station, related_name='prev_buses', on_delete=models.SET_NULL, null=True, blank=True)
    is_on_station = models.BooleanField(default=False)
    last_update_time = models.TimeField(auto_now=True)
    token = models.CharField(max_length=200)

    def __str__(self):
        name = self.line.name + " on station " + self.prev_station.name
        if not self.is_on_station:
            name += " to station " + self.next_station.name
        return name
