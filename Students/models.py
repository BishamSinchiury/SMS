from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class PersonInfo(models.Model):
    first_name = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    date_of_birth = models.DateField()
    gender = models.CharField(_("Gender"), max_length=50, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        _("Phone Number"),
        max_length=15,
        validators=[
            RegexValidator(r"^\+?1?\d{9,15}$", "Enter a valid phone number (up to 15 digits).")
        ],
    )
    nationality = models.CharField(_("Nationality"), max_length=50)

    class Meta:
        verbose_name = "Personal Info"
        verbose_name_plural = "Personal Infos"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class GuardianInfo(models.Model):
    father_name = models.CharField(_("Father's Name"), max_length=255)
    mother_name = models.CharField(_("Mother's Name"), max_length=255)
    guardian_name = models.CharField(_("Guardian's Name"), max_length=255)

    class Meta:
        verbose_name = "Guardian Info"
        verbose_name_plural = "Guardian Infos"

    def __str__(self):
        return f"Guardian: {self.guardian_name}"

class Address(models.Model):
    province = models.CharField(_("Province"), max_length=50)
    district = models.CharField(_("District"), max_length=50)
    local_body = models.CharField(_("Local Body"), max_length=50)
    ward = models.CharField(_("Ward"), max_length=10)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.local_body}, Ward {self.ward}, {self.district}, {self.province}"

class AcademicInfo(models.Model):
    level = models.ForeignKey("Admin.Level", on_delete=models.CASCADE, related_name="levels")
    grade = models.ForeignKey("Admin.Grade", on_delete=models.CASCADE, related_name="grades")
    section = models.ForeignKey("Admin.Section", on_delete=models.CASCADE, related_name="sections")
    faculty = models.ForeignKey("Admin.Faculty", on_delete=models.CASCADE, related_name="faculties")
    major = models.ForeignKey("Admin.Major", on_delete=models.CASCADE, related_name="majors")
    join_date = models.DateField()
    graduation_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Academic Info"
        verbose_name_plural = "Academic Infos"

    def clean(self):
        if self.graduation_date and self.graduation_date <= self.join_date:
            raise ValidationError("Graduation date must be after the join date.")


    def __str__(self):
        return f"{self.level} - {self.grade} ({self.faculty})"

class Student(models.Model):
    person_info = models.OneToOneField(PersonInfo, on_delete=models.CASCADE, related_name="student")
    guardian_info = models.OneToOneField(GuardianInfo, on_delete=models.CASCADE, related_name="student")
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name="student")
    academic_info = models.OneToOneField(AcademicInfo, on_delete=models.CASCADE, related_name="student")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f"Student: {self.person_info.first_name} {self.person_info.last_name}"


