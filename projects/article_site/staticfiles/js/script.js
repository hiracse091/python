/**
 * Created by Naher-DC on 8/24/2014.
 */

$(document).ready(function(){
    $('.readbtn').on('click',function(){
        console.log("worked");

    })
})
var my_app = angular.module('app',[]).config(function($httpProvider,$interpolateProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});