// グローバル変数の定義
var map = null ;		// 地図のインスタンス

// 地図の出力
function initialize()
{
	/* 変数の定義 */
	var canvas , latlng , mapOptions ;

	/* キャンパスの要素[<div id="map-canvas"></div>]を取得する */
	canvas = document.getElementById( 'map-canvas' );

	/* 中心座標を、LatLngクラスで用意する */
	latlng = new google.maps.LatLng( 34.645842,135.5139714 );

	/* Mapクラスのオプションを設定する */
	mapOptions = {
		zoom: 15 ,				//ズーム値
		center: latlng ,		//中心座標 [LatLngクラスで指定]
	} ;

	/* Mapクラスのインスタンスを作成する */
	map = new google.maps.Map( canvas , mapOptions ) ;

	/* イベントの作成 */

	google.maps.event.addListener( map , 'click' , function(event)
	{

		document.getElementById("show_lat").innerHTML = event.latLng.lat();
		document.getElementById("show_lng").innerHTML = event.latLng.lng();
	} ) ;
}

google.maps.event.addDomListener( window , 'load' , initialize ) ;
// マーカーのインスタンスは配列で管理しよう
var markers = [] ;

// マーカーのインスタンスを作成する
markers[0] = new google.maps.Marker({
	map: map ,
	position: new google.maps.LatLng( 35.792621 , 139.806513 ) ,
}) ;
