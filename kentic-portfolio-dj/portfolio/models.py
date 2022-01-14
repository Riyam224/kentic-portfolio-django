from django.db import models

# Create your models here.


from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse



class Post(models.Model):
    name = models.CharField(_("name"), max_length=50)
    img = models.ImageField(_("image"), upload_to='posts', blank=True , null=True)
    slug = models.SlugField(_("slug"), blank=True , null=True)
    created_at = models.DateTimeField(_("create at "), auto_now_add=True)

    

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def save(self , *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Post , self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})
