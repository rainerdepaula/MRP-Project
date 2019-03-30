from django.utils.translation import ugettext_lazy as _
from django.db import models
from system.constant import *


class ProductOrder(models.Model):
    client_name = models.CharField(_('Müşteri İsmi'), null=True, blank=True, max_length=150)
    name = models.CharField(_('Ürün İsmi'), null=True, blank=True, max_length=150)
    status = models.CharField(_('Ürün İsmi'), choices=PRODUCT_ORDER_STATUS, default=WAITING,  max_length=150)
    created_at = models.DateTimeField(_('Kayıt Tarihi'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_('Güncellenme Tarihi'), auto_now=True, editable=False)

    class Meta:
        verbose_name= _('Ürün Siparişi')
        verbose_name_plural = _('Ürün Siparişleri')
        ordering = ('-created_at',)

    def __str__(self):
        return '{}'.format(self.name)


class RawOrder(models.Model):
    name = models.CharField(_('Hammadde İsmi'), null=True, blank=True, max_length=150)
    status = models.CharField(_('Ürün İsmi'), choices=RAW_ORDER_STATUS, default=WAITING, max_length=150)
    created_at = models.DateTimeField(_('Kayıt Tarihi'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_('Güncellenme Tarihi'), auto_now=True, editable=False)

    class Meta:
        verbose_name= _('Hammadde Siparişi')
        verbose_name_plural = _('Hammadde Siparişleri')
        ordering = ('-created_at',)

    def __str__(self):
        return '{}'.format(self.name)


class Client(models.Model):
    email = models.EmailField('E-posta', unique=True, null=False, blank=False)
    name = models.CharField(_('İsim'), null=True, blank=True, max_length=150)
    surname = models.CharField('Soyisim', null=True, blank=True, max_length=75)
    phone = models.CharField('Telefon', null=True, blank=True, max_length=75)
    created_at = models.DateTimeField(_('Kayıt Tarihi'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_('Güncellenme Tarihi'), auto_now=True, editable=False)

    class Meta:
        verbose_name= _('Müşteri')
        verbose_name_plural = _('Müşteriler')
        ordering = ('-created_at',)

    def __str__(self):
        return '{}'.format(self.name)


class Supplier(models.Model):
    email = models.EmailField('E-posta', unique=True, null=False, blank=False)
    name = models.CharField(_('İsim'), null=True, blank=True, max_length=150)
    surname = models.CharField('Soyisim', null=True, blank=True, max_length=75)
    phone = models.CharField('Telefon', null=True, blank=True, max_length=75)
    created_at = models.DateTimeField(_('Kayıt Tarihi'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_('Güncellenme Tarihi'), auto_now=True, editable=False)

    class Meta:
        verbose_name= _('Tedarikçi')
        verbose_name_plural = _('Tedarikçiler')
        ordering = ('-created_at',)

    def __str__(self):
        return '{}'.format(self.name)