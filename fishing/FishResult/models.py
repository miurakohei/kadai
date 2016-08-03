from django.db import models


class rod_master(models.Model):
    """ロッドマスタ"""
    rod_id = models.IntegerField('商品ID',primary_key=True)
    length = models.IntegerField('長さ')


class reel_master(models.Model):
    """リールマスタ"""
    reel_id = models.IntegerField('商品ID',primary_key=True)
    wind_length = models.FloatField('巻き取り長さ')
    weight = models.FloatField('重さ')


class line_master(models.Model):
    """ラインマスタ"""
    line_id = models.IntegerField('商品ID',primary_key=True)
    type_size = models.FloatField('号数')


class rure_master(models.Model):
    """ルアーマスタ"""
    rure_id = models.IntegerField('商品ID',primary_key=True)
    weight = models.IntegerField('重さ')


class worm_master(models.Model):
    """ワームマスタ"""
    worm_id = models.IntegerField('商品ID',primary_key=True)
    inchi = models.IntegerField('長さ')


class gimmic_master(models.Model):
    """仕掛けマスタ"""
    gimmic_id = models.IntegerField('仕掛けID',primary_key=True)


class maker_master(models.Model):
    """メーカーマスタ"""
    maker_id = models.IntegerField("メーカーID", primary_key=True)
    maker_name = models.CharField("名称", max_length=200)


class use_master(models.Model):
    """用途マスタ"""
    use_id = models.IntegerField("用途ID", primary_key=True)
    use_name = models.CharField("名称", max_length=200)
    remarks = models.CharField("備考", max_length=200)


class user_master(models.Model):
    """ユーザマスタ"""
    user_id = models.CharField("ユーザID", primary_key=True, max_length=200)
    user_name = models. CharField("ユーザ名", max_length=200)


class product_master(models.Model):
    """商品マスタ"""
    product_id = models.IntegerField("商品ID", primary_key=True)
    product_name = models.CharField("名称", max_length=200)
    maker_id = models.ForeignKey(maker_master, verbose_name="メーカーID")
    use_id = models.ForeignKey(use_master, verbose_name="用途ID")
    create_date = models.DateField("登録日", auto_now=True)
    image = models.ImageField("画像", upload_to='images/')
    classification = models.IntegerField("区分")
    user_id = models.ForeignKey(user_master, verbose_name="ユーザID")


class set_master(models.Model):
    """セットマスタ"""
    set_id = models.IntegerField('セットID',primary_key=True)
    set_name = models.CharField('名称', max_length=200)
    rod_id = models.ForeignKey(rod_master, verbose_name="ロッドID",)
    reel_id=models.ForeignKey(reel_master, verbose_name="リールID",)
    line_id=models.ForeignKey(line_master, verbose_name="ラインID",)
    rure_id=models.ForeignKey(rure_master, verbose_name="ルアーID",)
    worm_id=models.ForeignKey(worm_master, verbose_name="ワームID",)
    gimmic_id=models.ForeignKey(gimmic_master, verbose_name="仕掛けID",)
    create_date=models.DateField("登録日", auto_now=True)
    image = models.ImageField("画像", upload_to='images/')
    user = models.CharField("登録者", max_length=200)


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
    set_id = models.ForeignKey(set_master, verbose_name="セットID")
    comment = models.CharField("コメント", max_length=200)
    latitude = models.FloatField("緯度",)
    longitude = models.FloatField("経度")
    create_time = models.DateField("登録時間",auto_now=True)
    image = models.ImageField("画像", upload_to='images/')
    user = models.CharField("登録者", max_length=200)
