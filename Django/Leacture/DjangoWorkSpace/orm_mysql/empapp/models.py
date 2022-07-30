from django.db import models

class Emp(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    address=models.TextField(max_length=300)

    def __str__(self):
        return self.name
        
class EmpQuali(models.Model):
    college=models.CharField(max_length=30)
    hsc=models.IntegerField()
    ssc=models.IntegerField()
    grad=models.IntegerField()
    description=models.TextField(max_length=400)
    emp=models.ForeignKey(Emp,on_delete=models.CASCADE)

    class Meta:
        db_table="emp_qualif"

class EmpQuali2(models.Model):
    college=models.CharField(max_length=30)
    hsc=models.IntegerField()
    ssc=models.IntegerField()
    grad=models.IntegerField()
    description=models.TextField(max_length=400)
    emp=models.OneToOneField(Emp,on_delete=models.CASCADE)

    class Meta:
        db_table="emp_qualif2"

class EmpQuali3(Emp):
    college=models.CharField(max_length=30)
    hsc=models.IntegerField()
    ssc=models.IntegerField()
    grad=models.IntegerField()
    description=models.TextField(max_length=400)

    class Meta:
        db_table="emp_qualif3"


class Singer(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    age=models.IntegerField()

    class Meta:
        db_table="singer"
class Songs(models.Model):
    name=models.CharField(max_length=30)
    duration=models.CharField(max_length=30)
    singer=models.ManyToManyField(Singer)

    class Meta:
        db_table="songs"