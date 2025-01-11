from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _

# Level Model

class InstitutionInfo(models.Model):
    name = models.CharField(_("name"), max_length=100)
    address = models.CharField(_("address"), max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    logo = models.ImageField(upload_to="media/logo")
    pan = models.CharField(max_length=50)

class Level(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinLengthValidator(2)],
        help_text=_("Name of the educational level, e.g., Primary, Secondary, etc.")
    )
    description = models.TextField(blank=True, null=True, help_text=_("Optional description of the level"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Level"
        verbose_name_plural = "Levels"

    def __str__(self):
        return self.name


# Grade Model
class Grade(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinLengthValidator(1)],
        help_text=_("Grade name or identifier, e.g., Grade 1, Grade 10, etc.")
    )
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="grades", help_text=_("Level this grade belongs to"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Grade"
        verbose_name_plural = "Grades"

    def __str__(self):
        return f"{self.level.name} - {self.name}"


# Section Model
class Section(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinLengthValidator(1)],
        help_text=_("Section name or identifier, e.g., A, B, etc.")
    )
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name="sections", help_text=_("Grade this section belongs to"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Section"
        verbose_name_plural = "Sections"

    def __str__(self):
        return f"{self.grade.name} - {self.name}"


# Faculty Model
class Faculty(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinLengthValidator(2)],
        help_text=_("Name of the faculty, e.g., Science, Arts, Commerce, etc.")
    )
    description = models.TextField(blank=True, null=True, help_text=_("Optional description of the faculty"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"

    def __str__(self):
        return self.name


# Subjects Model
class Subject(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinLengthValidator(2)],
        help_text=_("Name of the subject, e.g., Mathematics, Physics, etc.")
    )
    code = models.CharField(
        max_length=10,
        unique=True,
        validators=[MinLengthValidator(2)],
        help_text=_("Unique code for the subject, e.g., MATH101")
    )
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, related_name="subjects", help_text=_("Faculty this subject belongs to"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return f"{self.name} ({self.code})"


# Major Model
class Major(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinLengthValidator(2)],
        help_text=_("Name of the major, e.g., Computer Science, Biology, etc.")
    )
    description = models.TextField(blank=True, null=True, help_text=_("Optional description of the major"))
    subjects = models.ManyToManyField(Subject, related_name="majors", help_text=_("Subjects included in this major"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Major"
        verbose_name_plural = "Majors"

    def __str__(self):
        return self.name
