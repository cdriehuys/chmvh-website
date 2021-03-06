from django.db import models


def patient_image_path(instance, filename):
    """Generate the path to save a patient's image under.

    Args:
        instance (obj):
            The Patient instance that the file field belongs to.
        filename (str):
            The orignal filename of the uploaded image.

    Returns:
        str:
            The file path to upload the provided image to.
    """
    ext = filename.rsplit(".", 1)[-1]

    return "patients/{0}/{1}.{2}".format(
        instance.first_name[0].upper(), instance.first_name, ext
    )


def patient_thumbnail_path(instance, filename):
    parts = instance.picture.name.rsplit(".", 1)
    assert len(parts) == 2

    return "{0}_thumb.{1}".format(parts[0], parts[1])


class Patient(models.Model):
    """A veterinary patient with a name and picture."""

    deceased = models.BooleanField(
        default=False,
        help_text=(
            "Patients marked as deceased will have their picture "
            "displayed in the 'In Memoriam' section."
        ),
        verbose_name="deceased",
    )
    description = models.CharField(
        blank=True,
        help_text=(
            "For featured patients, their description will be "
            "displayed underneath their name on the gallery home "
            "page"
        ),
        max_length=100,
        verbose_name="featured description",
    )
    featured = models.BooleanField(
        default=False,
        help_text=(
            "Patients marked as featured will be displayed on the "
            "gallery home page."
        ),
        verbose_name="featured",
    )
    first_letter = models.CharField(max_length=1, verbose_name="first letter")
    first_name = models.CharField(max_length=100, verbose_name="first name")
    last_name = models.CharField(
        blank=True,
        help_text=(
            "This is only used to identify the patient, and is not "
            "displayed publicly."
        ),
        max_length=100,
        verbose_name="last name",
    )
    picture = models.ImageField(
        upload_to=patient_image_path, verbose_name="picture"
    )
    thumbnail = models.ImageField(
        null=True,
        upload_to=patient_thumbnail_path,
        verbose_name="picture thumbnail",
    )

    class Meta:
        ordering = ("first_name", "last_name")

    def __str__(self):
        """Return the patients name"""
        return "{fname} {lname}".format(
            fname=self.first_name, lname=self.last_name
        ).strip()

    def save(self, *args, **kwargs):
        self.first_letter = self.first_name[0].upper()

        return super(Patient, self).save(*args, **kwargs)
