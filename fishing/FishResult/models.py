from django.db import models


class rod_master(models.Model):
    """ロッドマスタ"""
    rod_id = models.IntegerField('商品ID',primary_key=True)
    rod_name = models.CharField('商品名', max_length=200)
    length = models.IntegerField('長さ(m)')

    def __str__(self):
        return self.rod_name


class reel_master(models.Model):
    """リールマスタ"""
    reel_id = models.IntegerField('商品ID',primary_key=True)
    reel_name = models.CharField('商品名', max_length=200)
    wind_length = models.FloatField('巻き取り長さ(m)')
    weight = models.FloatField('重さ(グラム)')

    def __str__(self):
        return self.reel_name


class line_master(models.Model):
    """ラインマスタ"""
    line_id = models.IntegerField('商品ID',primary_key=True)
    line_name = models.CharField('商品名', max_length=200)
    type_size = models.FloatField('号数')

    def __str__(self):
        return self.line_name


class rure_master(models.Model):
    """ルアーマスタ"""
    rure_id = models.IntegerField('商品ID',primary_key=True)
    rure_name = models.CharField('商品名', max_length=200)
    weight = models.IntegerField('重さ')

    def __str__(self):
        return self.rure_name


class worm_master(models.Model):
    """ワームマスタ"""
    worm_id = models.IntegerField('商品ID',primary_key=True)
    worm_name = models.CharField('商品名', max_length=200)
    inchi = models.IntegerField('長さ(インチ)')

    def __str__(self):
        return self.worm_name


class gimmic_master(models.Model):
    """仕掛けマスタ"""
    gimmic_id = models.IntegerField('仕掛けID',primary_key=True)
    gimmic_name = models.CharField('商品名', max_length=200)

    def __str__(self):
        return self.gimmic_name


class maker_master(models.Model):
    """メーカーマスタ"""
    maker_id = models.AutoField("メーカーID", primary_key=True)
    maker_name = models.CharField("名称", max_length=200)

    def __str__(self):
        return self.maker_name


class use_master(models.Model):
    """用途マスタ"""
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    use_id = models.AutoField("用途ID", primary_key=True, default=0)
=======
    use_id = models.AutoField("用途ID", primary_key=True)
>>>>>>> 8906134308927766bd4832eb6c2b019fd624c2ff
=======
    use_id = models.AutoField("用途ID", primary_key=True)
>>>>>>> 8906134308927766bd4832eb6c2b019fd624c2ff
=======
    use_id = models.AutoField("用途ID", primary_key=True)
>>>>>>> 8906134308927766bd4832eb6c2b019fd624c2ff
    use_name = models.CharField("名称", max_length=200)
    remarks = models.CharField("備考", max_length=200)

    def __str__(self):
        return self.use_name


class user_master(models.Model):
    """ユーザマスタ"""
    user_id = models.CharField("ユーザID", primary_key=True, max_length=200)
    user_name = models. CharField("ユーザ名", max_length=200)

    def __str__(self):
        return self.user_name

class product_master(models.Model):
    """商品マスタ"""

    CLASSIFICATION_CHOISES = (
        ('1','ロッド'),
        ('2','リール'),
        ('3','ライン'),
        ('4','ルアー'),
        ('5','ワーム'),
        ('6','仕掛け'),
    )

    product_id = models.AutoField("商品ID", primary_key=True)
    product_name = models.CharField("名称", max_length=200)
    maker_id = models.ForeignKey(maker_master, verbose_name="メーカーID",)
    use_id = models.ForeignKey(use_master, verbose_name="用途ID")
    create_date = models.DateField("登録日", auto_now=True)
    image = models.ImageField("画像", upload_to='images/', blank=True)
    classification = models.CharField("区分",max_length=2, choices=CLASSIFICATION_CHOISES)
    user_id = models.ForeignKey(user_master, verbose_name="ユーザID")


class set_master(models.Model):
    """セットマスタ"""
    set_id = models.AutoField('セットID',primary_key=True)
    set_name = models.CharField('名称', max_length=200)
    rod_id = models.ForeignKey(rod_master, verbose_name="ロッドID",)
    reel_id=models.ForeignKey(reel_master, verbose_name="リールID",)
    line_id=models.ForeignKey(line_master, verbose_name="ラインID",)
    rure_id=models.ForeignKey(rure_master, verbose_name="ルアーID", blank=True)
    worm_id=models.ForeignKey(worm_master, verbose_name="ワームID", blank=True)
    gimmic_id=models.ForeignKey(gimmic_master, verbose_name="仕掛けID", blank=True)
    create_date=models.DateField("登録日", auto_now=True)
    image = models.ImageField("画像", upload_to='images/', blank=True)
    user = models.CharField("登録者", max_length=200)

    def __str__(self):
        return self.set_name


class ownership_master(models.Model):
    """所有マスタ"""
    user_id =  models.CharField("ユーザID", primary_key=True, max_length=200)
    product_id = models.ForeignKey(product_master, verbose_name="商品ID")


class val_info_master(models.Model):
    """構成マスタ"""
    val_info_id = models.AutoField(primary_key=True,)
    classification = models.IntegerField("区分",)
    val_info_if = models.IntegerField("構成ID",)
    input_type = models.CharField("inputタイプ", max_length=200)
    input_name = models.CharField("input名称", max_length=200)
    dataset = models.CharField("dataset", max_length=200)

    class meta :
        unique_together=(("classification","val_info_master"))


class fish_result(models.Model):
    """釣果登録テーブル"""
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    result_id = models.AutoField("釣果ID", primary_key=True)
=======
    result_id =models.AutoField(primary_key=True)
>>>>>>> 8906134308927766bd4832eb6c2b019fd624c2ff
=======
    result_id =models.AutoField(primary_key=True)
>>>>>>> 8906134308927766bd4832eb6c2b019fd624c2ff
=======
    result_id =models.AutoField(primary_key=True)
>>>>>>> 8906134308927766bd4832eb6c2b019fd624c2ff
    set_id = models.ForeignKey(set_master, verbose_name="セット")
    comment = models.CharField("コメント", max_length=200, blank ='True')
    latitude = models.FloatField("緯度(地図をクリック)",)
    longitude = models.FloatField("経度(地図をクリック)")
    create_time = models.DateField("登録時間",auto_now=True)
    image = models.ImageField("画像", upload_to='images/', blank=True)
    user = models.ForeignKey(user_master, verbose_name="登録者")
