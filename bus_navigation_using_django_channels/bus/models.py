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
    line = models.ForeignKey(Line, related_name='buses', on_delete=models.CASCADE, null=True, blank=True)
    speed = models.FloatField(default=0.000535)
    x_pos = models.FloatField()
    y_pos = models.FloatField()
    prev_station = models.ForeignKey(Station, related_name='next_buses', on_delete=models.SET_NULL, null=True, blank=True)
    next_station = models.ForeignKey(Station, related_name='prev_buses', on_delete=models.SET_NULL, null=True, blank=True)
    is_on_station = models.BooleanField(default=False)
    last_update_time = models.TimeField(auto_now=True)
    token = models.CharField(max_length=200)

    def __str__(self):
        if self.line:
            line_name = self.line.name
        else:
            line_name = 'no line'
        if self.prev_station:
            prev_name = self.prev_station.name
        else:
            prev_name = 'no prev station'
        if self.next_station:
            next_name = self.next_station.name
        else:
            next_name = 'no next station'
        name = line_name + " on station " + prev_name
        if not self.is_on_station:
            name += " to station " + next_name
        return name
