var app = angular.module("app",["ngResource"]);

app.controller("controlador",function($scope, materia, datos){

	$scope.listamateria=materia.get();
	$scope.listaestudiante=datos.get();
	$scope.formulario=true;



	$scope.Validar = function(){
		var band = false;
		for (var i =0; i < $scope.listaestudiante.length;i++) {
			if($scope.cedula==$scope.listaestudiante[i].cedula)
					band = true;
	
			if(band){
					$scope.msg=false;
					$scope.materia=true;
					$scope.formulario=false;
			}
			else {
				$scope.msg=true;
				$scope.mensaje="No Registrado";		
			}
		}
	}

	$scope.matriculado = function(){
		$scope.msg=true;
		$scope.mensaje="Matricula Solicitada";

	}	

   


});


app.factory('materia', function($resource){
	return $resource("http://127.0.0.1:8000/materia/",{},
		{get:{method:"GET",pararms:{},isArray:true}}); 
		
	}
);


app.factory('datos',['$resource', function ($resource) {

	return $resource('http://127.0.0.1:8000/estudiante/',{},{get:{method:'GET', pararms:{}, isArray:true}
		});// body...
	}
]);


