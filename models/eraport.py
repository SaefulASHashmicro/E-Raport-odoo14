from odoo import api, fields, models,_


class Mapel(models.Model):
    _name = 'mapel'
    _description = 'Data Nilai'
    _order = 'n_matematika desc, n_senibudaya desc, n_bahasaindonesia desc'
    
    rank = fields.Char(string='Rangking')
    siswa = fields.Many2one(comodel_name='siswa', string='Nama')
    kelas_id = fields.Selection(string='Kelas', selection=[('x', 'X'), ('xi', 'XI'), ('xii', 'XII')], related='siswa.kelas')
    n_matematika = fields.Integer(string='Matematika')
    n_senibudaya = fields.Integer(string='Seni Budaya')
    n_bahasaindonesia = fields.Integer(string='Bahasa Indonesia')
    total = fields.Integer(compute='_get_sum', store=True)
    rerata = fields.Float(compute='_get_avg', store=True)
    
    
    @api.model
    def create(self, vals):
        if vals.get('rank', ('-')) == ('-'):
            vals['rank'] = self.env['ir.sequence'].next_by_code('mapel') or ('-')
        res = super(Mapel, self).create(vals)
        return res
    
    @api.depends('n_matematika', 'n_senibudaya', 'n_bahasaindonesia')

    def _get_sum(self):
        for rec in self:
           rec.update({
                'total': rec.n_matematika+rec.n_senibudaya+rec.n_bahasaindonesia,

            })
    
    @api.depends('n_matematika', 'n_senibudaya', 'n_bahasaindonesia')

    def _get_avg(self):
        for rec in self:
           rec.update({
                'rerata': rec.n_matematika+rec.n_senibudaya+rec.n_bahasaindonesia/3,

            })
class Siswa(models.Model):
    _name = 'siswa'
    _description = 'Data Siswa'
    _rec_name = 'nama_siswa'

    nama_siswa = fields.Char(string='Nama')
    kelas = fields.Selection(string='Kelas', selection=[('x', 'X'), ('xi', 'XI'), ('xii', 'XII')])
    tmp_lahir = fields.Char(string='Tempat Lahir')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    j_kel = fields.Selection(string='Jenis Kelamin', selection=[('L', 'Laki-laki'), ('P', 'Perempuan'),])
    nis = fields.Char(string='NIS')
    agama = fields.Selection(string='Agama', selection=[('islam', 'Islam'), ('kristen', 'Kristen'), ('budha', 'Budha'), ('konghucu', 'Konghucu')])