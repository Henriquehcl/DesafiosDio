/*
Desafio
Tento como base a hora inicial e final de um jogo, 
calcule a duração do dele, sabendo que o mesmo pode 
começar em um dia e terminar em outro, tendo uma duração 
mínima de, 60 minutos e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a 
hora de início e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo.
 */

import java.util.Scanner;

public class Problem {
	public static void main(String[] args){
		
               //complete os espaços em branco com sua solução para o problema           

                Scanner scan = new Scanner(System.in);
		int inicio, fim, horas;
		inicio = scan.nextInt();
		fim = scan.nextInt();


		if (inicio > fim) { 
			System.out.println("O JOGO DUROU " + (24 - (inicio - fim)) + " HORA(S)");
		} else if (inicio > fim) {
			System.out.println("O JOGO DUROU " + ( inicio - fim ) + " HORA(S)");
		} else if (inicio < fim) {
			System.out.println("O JOGO DUROU " + ( fim - inicio) + " HORA(S)");
		}else {
			System.out.println("O JOGO DUROU 24 HORA(S)");
		}
	}
}
