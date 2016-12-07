// グローバル変数の定義
var map = null ;
var markers	= [];	// 地図のインスタンス
var list = [];

// 地図の出力
function initialize()
{
	/* 変数の定義 */
	var canvas , latlng , mapOptions, markerOption ;

	/* キャンパスの要素[<div id="map-canvas"></div>]を取得する */
	canvas = document.getElementById( 'map-canvas' );

	/* 中心座標を、LatLngクラスで用意する */
	latlng = new google.maps.LatLng( 34.645842,135.5139714 );

	/* Mapクラスのオプションを設定する */
	mapOptions = {
		zoom: 8 ,				//ズーム値
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


	// マーカーのインスタンスを作成する
	// markers[0] = new google.maps.Marker({
	// 	map: map ,
	// 	position: new google.maps.LatLng( 34.645842,135.5139714 ) ,
	// }) ;

var list = document.getElementById( "markerlist" ).list;

// マーカーのインスタンスを作成する
for ( var i = 0; i < list.length; ++i ) {

	markers[i] = new google.maps.Marker({
		map: map ,
		position: new google.maps.LatLng( list[i].latitude , list[i].longitude ) ,
	}) ;
}
}

google.maps.event.addDomListener( window , 'load' , initialize ) ;
