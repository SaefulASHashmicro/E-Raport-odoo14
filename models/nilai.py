from odoo import api, fields, models


class matematika(models.Model):
    _name = 'matematika'
    _description = 'Data Nilai Matematika'

    peserta = fields.Many2one(comodel_name="siswa", string='Nama')
    kelas = fields.Selection(string='', selection=[('x', 'X'), ('xi', 'XI'), ('xii', 'XII')], related='peserta.kelas', store=True)
    j_kel = fields.Selection(string='Jenis Kelamin', selection=[('L', 'Laki-laki'), ('P', 'Perempuan'),] ,related='peserta.j_kel' ,store=True)
    total = fields.Integer(compute='_get_sum', store=True)
    rerata = fields.Float(compute='_get_avg', store=True)
    state = fields.Selection(string='State', selection=[('lulus', 'Lulus'), ('remidi', 'Remidi'),])
    
    # field ujian
    uk1 = fields.Integer(string='Ulangan ke 1')
    uk2 = fields.Integer(string='Ulangan ke 2')
    uk3 = fields.Integer(string='Ulangan ke 3')
    uts = fields.Integer(string='UTS')
    uas = fields.Integer(string='UAS')
    
    @api.depends('uk1', 'uk2', 'uk3', 'uts', 'uas')
    def _get_sum(self):
        for rec in self:
           rec.update({
                'total': rec.uk1+rec.uk2+rec.uk3+rec.uts+rec.uas,

            })
               
    @api.depends('uk1', 'uk2', 'uk3', 'uts', 'uas')
    def _get_avg(self):
        for rec in self:
           rec.update({
                'rerata': rec.uk1+rec.uk2+rec.uk3+rec.uts+rec.uas/5,

            })         
                    
class senibudaya(models.Model):
    _name = 'senibudaya'
    _description = 'Data Nilai Seni Budaya'

    peserta = fields.Many2one(comodel_name='siswa', string='Nama')
    kelas = fields.Selection(string='', selection=[('x', 'X'), ('xi', 'XI'), ('xii', 'XII')], related='peserta.kelas', store=True)
    j_kel = fields.Selection(string='Jenis Kelamin', selection=[('L', 'Laki-laki'), ('P', 'Perempuan'),] ,related='peserta.j_kel' ,store=True)
    total = fields.Integer(compute='_get_sum', store=True)
    rerata = fields.Float(compute='_get_avg', store=True)
    state = fields.Selection(string='State', selection=[('lulus', 'Lulus'), ('remidi', 'Remidi'),] , compute='htg_ujian')
    
    # field ujian
    uk1 = fields.Integer(string='Ulangan ke 1')
    uk2 = fields.Integer(string='Ulangan ke 2')
    uk3 = fields.Integer(string='Ulangan ke 3')
    uts = fields.Integer(string='UTS')
    uas = fields.Integer(string='UAS')
    
    @api.depends('uk1', 'uk2', 'uk3', 'uts', 'uas')
    def _get_sum(self):
        for rec in self:
           rec.update({
                'total': rec.uk1+rec.uk2+rec.uk3+rec.uts+rec.uas,

            })
           
    @api.depends('uk1', 'uk2', 'uk3', 'uts', 'uas')
    def _get_avg(self):
        for rec in self:
           rec.update({
                'rerata': rec.uk1+rec.uk2+rec.uk3+rec.uts+rec.uas/5,

            })
                     
class bahasaindonesia(models.Model):
    _name = 'bahasaindonesia'
    _description = 'Data Nilai Bahasa Indonesia'

    peserta = fields.Many2one(comodel_name='siswa', string='Nama')
    kelas = fields.Selection(string='', selection=[('x', 'X'), ('xi', 'XI'), ('xii', 'XII')], related='peserta.kelas', store=True)
    j_kel = fields.Selection(string='Jenis Kelamin', selection=[('L', 'Laki-laki'), ('P', 'Perempuan'),] ,related='peserta.j_kel' ,store=True)
    total = fields.Integer(compute='_get_sum', store=True)
    rerata = fields.Float(compute='_get_avg', store=True)
    state = fields.Selection(string='State', selection=[('lulus', 'Lulus'), ('remidi', 'Remidi'),] , compute='htg_ujian')
    
    # field ujian
    uk1 = fields.Integer(string='Ulangan ke 1')
    uk2 = fields.Integer(string='Ulangan ke 2')
    uk3 = fields.Integer(string='Ulangan ke 3')
    uts = fields.Integer(string='UTS')
    uas = fields.Integer(string='UAS')
    
    @api.depends('uk1', 'uk2', 'uk3', 'uts', 'uas')
    def _get_sum(self):
        for rec in self:
           rec.update({
                'total': rec.uk1+rec.uk2+rec.uk3+rec.uts+rec.uas,

            })
           
    @api.depends('uk1', 'uk2', 'uk3', 'uts', 'uas')
    def _get_avg(self):
        for rec in self:
           rec.update({
                'rerata': rec.uk1+rec.uk2+rec.uk3+rec.uts+rec.uas/5,

            })

    @api.depends('state','uk1', 'uk2', 'uk3', 'uts', 'uas')
    def htg_ujian(self):
        for rec in self:
            if rec.rerata >= 300.00:
                return self.write({'state': 'lulus'}) 
            if rec.rerata <= 300.00:
                return self.write({'state': 'remidi'}) 
    
    # @api.depends('state')
    # def htg_ujian(self):
    #     for rec in self:
    #         if self.rerata > 300.00:
    #             return self.write({'state': 'lulus'})   
    
    # @api.depends('state')
    # def htg_ujian(self):
    #     if self.rerata > 300.00:
    #         return self.write({'state': 'remidi'})      
    
                     
    # @api.depends('state','uh1', 'uh2', 'uh3', 'uts', 'uas')
    # def htg_ujian(self):  
    #     for rec in self:
    #         if rec.rerata > 300.00:
    #             return self.write({'state': 'lulus'}) 
    #         if rec.rerata < 300.00:
    #             return self.write({'state': 'remidi'}) 