# MapAPI
MapAPI调用

# Google Mapapi summary：

Api中Distance Matrixモジュールで簡単に操作できる、距離情報と移動時間情報を全部得られる。

googlemapsをinstall必要です。

apikeyの申請必要です。

手順：

1.Google Cloud Platformでプロジェクトを立って、google mapページで Distance Matrix api をactive するー＞一方、google はapi keyを自動的に発行する

2.googlemapsをinstallする

3.計算パラメータをDistanceMatrixServiceに設定する（
origins（出発点　経度緯度可）、destinations（到着点　経度緯度可）、travelMode（交通方式：BICYCLING、DRIVING（Default Value）、TRANSIT（別のtransitOptionsパラメータ設定必要）、WALKING）、unitSystem（距離單位）
）

4.計算を得られた必要距離と必要時間パラメータがRow elementで見られる

5.複数到着点設定できる

お勧め順位：高

お金の心配がないユーザーのために安心サービスを提供する

GoogleMAPApiの更新とサポートは一番多いです。

ユーザーも一番多いで、全世界に使うことができる。

googlemapsのモジュールを提供する。簡単で使用して、計算結果を得られる

パラメータを細かいところも設定できるし、使い方と目標によって、弾力性をもつ。

交通渋滞の状況を含まれなら、extra feeで支払わなければならない(advance distance matrix使う場合)

MONETのgcpの環境で簡単に使用しても、Api申請必要があります。

ですけど、使用料金も一番多い、ユーザーと使用料によって、検討しないといけないです。


# Bing Mapapi summary

アカウントが必要です。

https://www.bingmapsportal.com/Application#　中にkey申請必要です。

手順：

1.post request の形でapi を使う、必要なパラメータ（origins（出発点　経度緯度可）、destinations（到着点　経度緯度可）、travelMode（交通方式：BICYCLING、DRIVING（Default Value）））を入力して、requestをhttpに送信する。

2.response文中に距離計算結果をえられる。

お勧め順位：低

BingMapは大手マップ会社ですけど、使用はHttpRequestが必要で、またMAPApiサポートは充実ではないが、無料使用量も少ないです。

マイクロソフトBingMapに基づいてのAPIです。

日本のユーザーは少ないです。サポートはgoogleより少ないです。

相談は英語が必要です。

APIの手動enableが必要です。注意！

GoogleDistanceMatrixとOSMDistanceMatrixと違うと、モジュールを提供していないので、JsonでPostRequestを送信必要です。計算結果の取るはresponse文中にやる必要があります。

試用期間があります。無料トランザクションは一番低いですけど、一日と一分間制限がなし。

有料は相談必要です。

# OpenStreetMap  Mapapi summary

routingpyをintall が必要です。

一般の形[Lat,Lon]　&　ORSの形[Lon,Lat]注意！

距離計算結果を0に計算したら、エラーが出っている（解決策：try catch の形で0のエラーをcatchして、数値0を直接にアウトプット）注意！

手順：

routingpy中のORS（open route service）を使用する

ORSのapikeyを引用して、travelModeパラメータを設定して、サービスを提供する。

origins（出発点　経度緯度）、destinations（到着点　経度緯度）

Open Street Mapのマップデータを自動用いて、route.distance（距離計算結果）とroute.duration（時間計算）を計算する。

お勧め順位：中 

個人開発ですけど、基本機能がもつ、モジュールがありますで簡単で使うし、無料使用量が一番多いです。

OpenStreetMapはオープンソースのマップです。

開発の目標はGoogleとBingの市場占有を破れことです。

OpenStreetMapに基づいて、距離計算は色んなAPIがあります。有料と無料はどちらでもあります。

ORSは無料のAPIです。個人で開発ものです。無料の使用量が一番多いですけど、一日と一分間制限があります。有料ユーザーは寄付金を支払う形で相談必要です。

ORSモジュールが提供して、簡単で計算結果を得られる。

基本機能が付いてですが、細かいパラメータ（例：距離計算結果単位）を調整できないです。
