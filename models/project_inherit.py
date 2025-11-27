from odoo import models, fields

class ProjectIHT(models.Model):
    _inherit = "project.project"

    lokasi_proyek = fields.Text(string="Lokasi Proyek")
    source_aplikasi_pendukung = fields.Char(string="Aplikasi Pendukung", help="Masukkan URL",)
    daftar_perkerja_remote = fields.Json(string="Daftar Pekerja Remote")
