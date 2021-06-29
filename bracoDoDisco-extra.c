#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int cmpfunc (const void * a, const void * b) {//função para auxilar no qsort
   return ( *(int*)a - *(int*)b );
}


int algoritmoDoElevador(char *arr){
    int bordaDoDisco,quantElemento,elementoInicial,posDoElementoInicial,soma;
    int flagBordaDoDisco;
    int tamanhoString,i;
    flagBordaDoDisco = 0;
    quantElemento = 0;//quantidade de elementos que foram passados
    tamanhoString = strlen(arr);//tamanho da string de entrada

	for(i=0;i< tamanhoString;i++){
		if(arr[i]==' '){
            quantElemento++;//quantidade de numeros no vetor menos a primeira entrada
          }
	}
    
   int vetorElementos[quantElemento];//vetor que guardara os elementos +1 contando com o elemento inicial que é a borda do disco
   int contador;//contador para o vetor de elementos
   contador = 0;
   
   //Split de todos numeros passados
   char * token = strtok(strdup(arr), " ");//split da string passada
   bordaDoDisco = atoi(token);//pega o primeiro numero que é a borda do disco
   while( token != NULL ) {//while necessario para fazer o split
      //printf( " %s\n", token ); //printing each token
      if(atoi(token)>bordaDoDisco){//se algum elemento for maior que a borda do disco...
		flagBordaDoDisco = 1;
		break;  
	  }
      token = strtok(NULL, " ");
      vetorElementos[contador] = atoi(token);//pega todos elementos menos o primeiro
      contador++;
   }
   
   
   if(flagBordaDoDisco == 1){ //entao é porque a entrada passada é maior que a borda do disco entao não pode
		return -1;
   }
   
   elementoInicial = vetorElementos[0];//primeiro elemento, antes de ordenar
   
   qsort(vetorElementos, quantElemento, sizeof(int), cmpfunc);//função que ordena a entrada em ordem crescente
   
   for(i=0;i<quantElemento;i++){
   	
		   if(vetorElementos[i]==elementoInicial){
			posDoElementoInicial = i; //indice do elemento inicial no vetor ordenado
            break;
	   }
   }
   

   soma = 0;
   for (i=posDoElementoInicial;i<quantElemento-1;i++){//todos elementos a frente do elemento inicial no vetor ordenado
		  soma+=abs(vetorElementos[i+1]-vetorElementos[i]);//ou seja vai no sentido mais externo do disco
   }
  
      
   for (i=posDoElementoInicial;i>0;i--){
		  if (i==posDoElementoInicial){//condicao para pegar o ultimo elemento do loop anterior e subtrair com o anterior do primeiro elemento
			 soma += abs(vetorElementos[quantElemento-1] - vetorElementos[i-1]);
		  }
		  else{
			  soma += abs(vetorElementos[i]-vetorElementos[i-1]);
		  }
   }

	return soma;
}

int main() {
    int resultado;

    resultado=algoritmoDoElevador("199 53 98 183 37 122 14 124 65 67");
    int nDigits = floor(log10(abs(resultado))) + 1;
    char resultadoEmString[nDigits];
    
    itoa(resultado,resultadoEmString,10);
    if(resultado!=-1){//se todos passados forem menores que a borda do disco é porque deu certo.
    	printf("Movimentacoes do braco do disco: %s",resultadoEmString);
	}
    return 0;
}
  