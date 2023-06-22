from django.db import models

class City(models.Model):
    city_seq = models.CharField(max_length = 7, primary_key = True)
    city_name = models.CharField(max_length = 10)
    
    class Meta:
        db_table = "city"
        verbose_name = "도시"
        verbose_name_plural = "도시 그룹"
        
        ordering = ['city_seq']
    

class Borough(models.Model):
    borough_seq = models.CharField(max_length = 9, primary_key = True)
    borough_name = models.CharField(max_length = 10)
    city_seq = models.ForeignObject("City", on_delete = models.PROTECT, db_column = "city_seq")
    
    class Meta:
        db_table = "borough"
        verbose_name = "구"
        verbose_name_plural = "구 그룹"
        
        ordering = ['city_seq', 'borough_seq']


class Theater(models.Model):
    theater_seq = models.CharField(max_length = 6, primary_key = True)
    theater_address = models.TextField()
    theater_type = models.TextChoices("CGV", "롯데시네마", "메가박스")
    theater_status = models.TextChoices("영업", "휴업", "폐업")
    theater_lat = models.DecimalField()
    theater_lng = models.DecimalField()
    
    borough_seq = models.ForeignObject("Borough", on_delete = models.PROTECT, db_column = "borough_seq")
    
    class Meta:
        db_table = "theater"
        verbose_name = "영화관"
        verbose_name_plural = "영화관 그룹"
        
        ordering = ['borough_seq', 'theater_seq']