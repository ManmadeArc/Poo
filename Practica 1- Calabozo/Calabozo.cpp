#include <iostream>
#include <vector>
#include<stdlib.h>
#include<time.h>
#include <conio.h>
#include<stdio.h>
#include <Windows.h>
#include <string>

using namespace std;



string opc;
string lado;
char guion = 92;
bool Game; //True = 1 jg False = 2j
vector<int> NumPool;
bool TerminarJuego = false;

bool EstadoCasD[11];
bool EstadoCasI[11];


int CasillasD[11];
int CasillasI[11];
int PuntajeDer=0;
int PuntajeIzq=0;
bool JugadorIzq;
bool BombaDer=false;
bool BombaIzq=false;
int PosJI=-1;
int PosJD=-1;
string Mov;


void GameMode();
void PrintTable();
void GenerarNumeros();
void gotoxy(int x, int y);
void LLenarPos(int i);
void OrganizarNum();
void GenerarBomba();
void SeleccionarLado();
void MoverIzq();
void MoverDer();
void IA();
void VictoriaPvP();
void VictoriaPvE();
void Reiniciar();


int main() {	
	srand(time(NULL));
	

	
	
	


	while (true)
	{
		system("cls");
		Reiniciar();
		GameMode();
		if (TerminarJuego) {
			return 0;
		}
		if (!Game) {
			system("cls");
			GenerarNumeros();
			OrganizarNum();
			GenerarBomba();
			SeleccionarLado();
			system("cls");
			PrintTable();
			cout << endl;

			if (JugadorIzq)
			{
				
				cout << "El Jugador 1 Comienza\n";

				for (int i = 0; i < 5; i++) {
					cout << "Jugador 1 Haga su movimiento\n";
					MoverIzq();
					cout << "Jugador 2 Haga su movimiento\n";
					MoverDer();

				}
				VictoriaPvP();
			}
			else {
				cout << "El Jugador 2 Comienza\n";
				for (int i = 0; i < 5; i++) {
					cout << "Jugador 2 Haga su movimiento\n";
					MoverIzq();
					cout << "Jugador 1 Haga su movimiento\n";
					MoverDer();

				}
				VictoriaPvP();
			}
		}
		else if (Game) {
			system("cls");
			GenerarNumeros();
			OrganizarNum();
			GenerarBomba();
			SeleccionarLado();
			system("cls");

			
			PrintTable();
			cout << endl;
		
			if (JugadorIzq)
			{
				cout << "El Jugador 1 Comienza\n";

				for (int i = 0; i < 5; i++) {
					
					
					cout << "Jugador 1 Haga su movimiento\n";
					MoverIzq();
					cout << "Maquina Haga su movimiento\n";
					IA();

				}
				VictoriaPvE();
			}
			else {
				cout << "La Maquina Comienza\n";
				for (int i = 0; i < 5; i++) {
					cout << "Maquina Haga su movimiento\n";
					IA();
					cout << "Jugador 1 Haga su movimiento\n";
					MoverDer();

				}
				VictoriaPvE();
			}
		}
		else {
			cout << "Opcion Inexistente\n";
			Sleep(2000);
			system("cls");
		}
		
		system("pause>nul");
	}
	

	

	
}

void Reiniciar() {
	for (int i = 0; i < 11; i++) {
		EstadoCasD[i] = false;
		EstadoCasI[i] = false;
		CasillasI[i] = 0;
		CasillasD[i] = 0;
	}
	NumPool.clear();
	PosJI = -1;
	PosJD = -1;
	BombaDer = false;
	BombaIzq = false;
	PuntajeDer = 0;
	PuntajeIzq = 0;
}

void VictoriaPvP(){
	if (BombaDer) {
		PuntajeDer = PuntajeDer / 2;
	}
	if (BombaIzq) {
		PuntajeIzq = PuntajeIzq / 2;
	}

	if (JugadorIzq) {
		if (PuntajeIzq > PuntajeDer) {
			cout << "El ganador es el Jugador 1 con " << PuntajeIzq << " puntos vs " << PuntajeDer <<" puntos\n";
		}
		else  if (PuntajeIzq<PuntajeDer){
			cout << "El ganador es el Jugador 2 con " << PuntajeDer << " puntos vs " << PuntajeIzq << " puntos\n";
		}
	else {
		cout << "Ambos jugadores han empatado a " << PuntajeDer << " puntos\n";
	}
	}
	else {
		if (PuntajeIzq > PuntajeDer) {
			cout << "El ganador es el Jugador 2 con " << PuntajeIzq << " puntos vs " << PuntajeDer << " puntos\n";
		}
		else if (PuntajeDer>PuntajeIzq) {
			cout << "El ganador es el Jugador 1 con " << PuntajeDer << " puntos vs " << PuntajeIzq << " puntos\n";
		}
	else {
		cout << "Ambos jugadores han empatado a " << PuntajeDer << " puntos\n";
	}
	}
}

void VictoriaPvE() {
	if (BombaDer) {
		PuntajeDer = PuntajeDer / 2;
	}
	if (BombaIzq) {
		PuntajeIzq = PuntajeIzq / 2;
	}

	if (JugadorIzq) {
		if (PuntajeIzq > PuntajeDer) {
			cout << "El ganador es el Jugador 1 con " << PuntajeIzq << " puntos vs " << PuntajeDer << " puntos\n";
		}
		else if (PuntajeIzq<PuntajeDer) {
			cout << "El ganador es la Maquina con " << PuntajeDer << " puntos vs " << PuntajeIzq << " puntos\n";
		}
	else {
		cout << "Ambos jugadores han empatado a " << PuntajeDer << " puntos\n";
	}
	}
	else {
		if (PuntajeIzq > PuntajeDer) {
			cout << "El ganador es la Maquina con " << PuntajeIzq << " puntos vs " << PuntajeDer << " puntos\n";
		}
		else if (PuntajeDer>PuntajeIzq){
			cout << "El ganador es el Jugador 1 con " << PuntajeDer << " puntos vs " << PuntajeIzq << " puntos\n";
		}
		else {
			cout << "Ambos jugadores han empatado a " << PuntajeDer << " puntos\n";
		}
	}
}

void IA() {

	if (!JugadorIzq) {
		if (PosJI == -1) {
			while (true)
			{
				cout << "Maquina Selecionando...\n";  Sleep(3000);
				Mov = to_string(1 + rand() % (2));
				if (Mov == "1") {
					PosJI += 1;
					break;
				}
				else if (Mov == "2") {
					PosJI += 2;
					break;
				}
			}
		}
		else if (PosJI == 0) {
			while (true)
			{
				cout << "Maquina Selecionando...\n";  Sleep(3000);
				Mov = to_string(1 + rand() % (2));
				if (Mov == "1") {
					PosJI += 2;
					break;
				}
				else if (Mov == "2") {
					PosJI += 3;
					break;
				}
			}
		}
		else if (PosJI == 1) {
			while (true)
			{
				cout << "Maquina Selecionando...\n";  Sleep(3000);
				Mov = to_string(1 + rand() % (2));
				if (Mov == "1") {
					PosJI += 2;
					break;
				}
				else if (Mov == "2") {
					PosJI += 3;
					break;
				}
			}
		}
		else if (PosJI == 2 || PosJI == 5) {
			while (true)
			{
				cout << "Maquina Selecionando...\n";  Sleep(3000);
				Mov = to_string(1 + rand() % (2));
				if (Mov == "1") {
					PosJI += 3;
					break;
				}
				else if (Mov == "2") {
					PosJI += 4;
					break;
				}
			}
		}
		else if (PosJI == 4 || PosJI == 7) {
			while (true)
			{
				cout << "Maquina Selecionando...\n";  Sleep(3000);
				Mov = to_string(1 + rand() % (2));
				if (Mov == "1") {
					PosJI += 2;
					break;
				}
				else if (Mov == "2") {
					PosJI += 3;
					break;
				}
			}
		}
		else if (PosJI == 3 || PosJI == 6) {
			while (true)
			{
				cout << "Maquina Selecionando...\n";  Sleep(3000);
				Mov = to_string(1 + rand() % (3));
				if (Mov == "1") {
					PosJI += 2;
					break;
				}
				else if (Mov == "2") {
					PosJI += 3;
					break;

				}
				else if (Mov == "3") {
					PosJI += 4;
					break;
				}
			}
		}
		else if (PosJI == 8 || PosJI == 9 || PosJI == 10) {
			while (true)
			{
				cout << "Maquina Selecionando...\n"; Sleep(3000);
				Mov = "1";
				if (Mov == "1") {
					PosJI = 11;
					break;
				}

			}
		}

		if (PosJI >= 0 && PosJI <= 10) {

			if (CasillasI[PosJI] <= 20) {
				PuntajeIzq += CasillasI[PosJI];
			}
			else if (CasillasI[PosJI]==99) {
				BombaIzq = true;
			}
		}
		system("cls");
		PrintTable();




	}
	else   {
	if (PosJD == -1) {
		while (true)
		{
			cout << "Maquina Selecionando...\n";  Sleep(3000);
			Mov = to_string(1 + rand() % (2));
			if (Mov == "1") {
				PosJD += 1;
				break;
			}
			else if (Mov == "2") {
				PosJD += 2;
				break;
			}
		}
	}
	else if (PosJD == 0) {
		while (true)
		{
			cout << "Maquina Selecionando...\n";  Sleep(3000);
			Mov = to_string(1 + rand() % (2));
			if (Mov == "1") {
				PosJD += 2;
				break;
			}
			else if (Mov == "2") {
				PosJD += 3;
				break;
			}
		}
	}
	else if (PosJD == 1) {
		while (true)
		{
			cout << "Maquina Selecionando...\n";  Sleep(3000);
			Mov = to_string(1 + rand() % (2));
			if (Mov == "1") {
				PosJD += 2;
				break;
			}
			else if (Mov == "2") {
				PosJD += 3;
				break;
			}
		}
	}
	else if (PosJD == 2 || PosJD == 5) {
		while (true)
		{
			cout << "Maquina Selecionando...\n";  Sleep(3000);
			Mov = to_string(1 + rand() % (2));
			if (Mov == "1") {
				PosJD += 3;
				break;
			}
			else if (Mov == "2") {
				PosJD += 4;
				break;
			}
		}
	}
	else if (PosJD == 4 || PosJD == 7) {
		while (true)
		{
			cout << "Maquina Selecionando...\n";  Sleep(3000);
			Mov = to_string(1 + rand() % (2));
			if (Mov == "1") {
				PosJD += 2;
				break;
			}
			else if (Mov == "2") {
				PosJD += 3;
				break;
			}
		}
	}
	else if (PosJD == 3 || PosJD == 6) {
		while (true)
		{
			cout << "Maquina Selecionando...\n";  Sleep(3000);
			Mov = to_string(1 + rand() % (3));
			if (Mov == "1") {
				PosJD += 2;
				break;
			}
			else if (Mov == "2") {
				PosJD += 3;
				break;

			}
			else if (Mov == "3") {
				PosJD += 4;
				break;
			}
		}
	}
	else if (PosJD == 8 || PosJD == 9 || PosJD == 10) {
		while (true)
		{
			cout << "Maquina Selecionando...\n"; Sleep(3000);
			Mov = "1";
			if (Mov == "1") {
				PosJD = 11;
				break;
			}

		}
	}

	if (PosJD >= 0 && PosJD <= 10) {

		if (CasillasD[PosJD] <= 20) {
			PuntajeDer += CasillasD[PosJD];
		}
		else if (CasillasD[PosJD] == 99) {
			BombaDer = true;
		}
	}
	system("cls");
	PrintTable();

	}



}

void MoverIzq() {
		if (PosJI == -1) {
			while (true)
			{
				cout << "Seleccione su Movimiento:\n[1]Mover Diagonal Superior\n[2]Mover Diagonal Inferior\n";
				cin >> Mov;
				if (Mov == "1") {
					PosJI += 1;
					break;
				}
				else if (Mov == "2") {
					PosJI += 2;
					break;
				}
			}
		}
		else if (PosJI == 0) {
			while (true)
			{
				cout << "Seleccione su Movimiento:\n[1]Mover Diagonal Superior\n[2]Mover Diagonal Inferior\n";
				cin >> Mov;
				if (Mov == "1") {
					PosJI += 2;
					break;
				}
				else if (Mov == "2") {
					PosJI += 3;
					break;
				}
			}
		}
		else if (PosJI == 1) {
			while (true)
			{
				cout << "Seleccione su Movimiento:\n[1]Mover Diagonal Superior\n[2]Mover Diagonal Inferior\n";
				cin >> Mov;
				if (Mov == "1") {
					PosJI += 2;
					break;
				}
				else if (Mov == "2") {
					PosJI += 3;
					break;
				}
			}
		}
		else if (PosJI == 2 || PosJI == 5) {
			while (true)
			{
				cout << "Seleccione su Movimiento:\n[1]Mover Adelante\n[2]Mover Diagonal Inferior\n";
				cin >> Mov;
				if (Mov == "1") {
					PosJI += 3;
					break;
				}
				else if (Mov == "2") {
					PosJI += 4;
					break;
				}
			}
		}
		else if (PosJI == 4 || PosJI == 7) {
			while (true)
			{
				cout << "Seleccione su Movimiento:\n[1]Mover Diagonal Superior\n[2]Mover Adelante\n";
				cin >> Mov;
				if (Mov == "1") {
					PosJI += 2;
					break;
				}
				else if (Mov == "2") {
					PosJI += 3;
					break;
				}
			}
		}
		else if (PosJI == 3 || PosJI == 6) {
				while (true)
				{
					cout << "Seleccione su Movimiento:\n[1]Mover Diagonal Superior\n[2]Mover Adelante\n[3]Mover Diagonal Inferior\n";
					cin >> Mov;
					if (Mov == "1") {
						PosJI += 2;
						break;
					}
					else if (Mov == "2") {
						PosJI += 3;
						break;

					}
					else if (Mov == "3") {
						PosJI += 4;
						break;
					}
				}
			}
		else if (PosJI == 8 || PosJI == 9 || PosJI==10) {
				while (true)
				{
					cout << "Seleccione su Movimiento:\n[1]Avanzar a la Meta\n";
					cin >> Mov;
					if (Mov == "1") {
						PosJI = 11;
						break;
					}
				
				}
			}
	
			if (PosJI >= 0 && PosJI <= 10) {

				if (CasillasI[PosJI] <= 20) {
					PuntajeIzq += CasillasI[PosJI];
				}
				else if(CasillasI[PosJI] == 99) {
					BombaIzq = true;
				}
			}
			system("cls");
			PrintTable();
	
}

void MoverDer() {
	if (PosJD == -1) {
		while (true)
		{
			cout << "Seleccione su Movimiento:\n[1]Mover Diagonal Superior\n[2]Mover Diagonal Inferior\n";
			cin >> Mov;
			if (Mov == "1") {
				PosJD += 1;
				break;
			}
			else if (Mov == "2") {
				PosJD += 2;
				break;
			}
		}
	}
	else if (PosJD == 0) {
		while (true)
		{
			cout << "Seleccione su Movimiento:\n[1]Mover Diagonal Superior\n[2]Mover Diagonal Inferior\n";
			cin >> Mov;
			if (Mov == "1") {
				PosJD += 2;
				break;
			}
			else if (Mov == "2") {
				PosJD += 3;
				break;
			}
		}
	}
	else if (PosJD == 1) {
		while (true)
		{
			cout << "Seleccione su Movimiento:\n[1]Mover Diagonal Superior\n[2]Mover Diagonal Inferior\n";
			cin >> Mov;
			if (Mov == "1") {
				PosJD += 2;
				break;
			}
			else if (Mov == "2") {
				PosJD += 3;
				break;
			}
		}
	}
	else if (PosJD == 2 || PosJD == 5) {
		while (true)
		{
			cout << "Seleccione su Movimiento:\n[1]Mover Adelante\n[2]Mover Diagonal Inferior\n";
			cin >> Mov;
			if (Mov == "1") {
				PosJD += 3;
				break;
			}
			else if (Mov == "2") {
				PosJD += 4;
				break;
			}
		}
	}
	else if (PosJD == 4 || PosJD == 7) {
		while (true)
		{
			cout << "Seleccione su Movimiento:\n[1]Mover Diagonal Superior\n[2]Mover Adelante\n";
			cin >> Mov;
			if (Mov == "1") {
				PosJD += 2;
				break;
			}
			else if (Mov == "2") {
				PosJD += 3;
				break;
			}
		}
	}
	else if (PosJD == 3 || PosJD == 6) {
		while (true)
		{
			cout << "Seleccione su Movimiento:\n[1]Mover Diagonal Superior\n[2]Mover Adelante\n[3]Mover Diagonal Inferior\n";
			cin >> Mov;
			if (Mov == "1") {
				PosJD += 2;
				break;
			}
			else if (Mov == "2") {
				PosJD += 3;
				break;

			}
			else if (Mov == "3") {
				PosJD += 4;
				break;
			}
		}
	}
	else if (PosJD == 8 || PosJD == 9 || PosJD == 10) {
		while (true)
		{
			cout << "Seleccione su Movimiento:\n[1]Avanzar a la Meta\n";
			cin >> Mov;
			if (Mov == "1") {
				PosJD = 11;
				break;
			}

		}
	}
	if (PosJD >= 0 && PosJD <= 10) {
		if (CasillasD[PosJD] <= 20) {
			PuntajeDer += CasillasD[PosJD];
		}
		else if (CasillasD[PosJD] == 99) {
			BombaDer = true;
		}
	}

	system("cls");
	PrintTable();
}

void GameMode() {
	cout << "Seleccione el modo de juego:\n [1] Player vs Player\n [2]Player vs Maquina\n [3]Terminar Juego\n";
	cin >> opc;
	if (opc == "1") {
		Game = false;
	}
	else if (opc == "2") {
		Game = true;
	}
	else if (opc == "3") {
		TerminarJuego = true;
	}
	else {
		system("cls");
		GameMode();
	}
}


void SeleccionarLado() {
	
	while (true) {
		cout << "Jugador 1 Introduzca el lado del tablero a utilizar\n[1]Derecha\n[2]Izquierda\n";
		cin >> lado;
		if (lado == "1") {
			JugadorIzq = false;
			break;
		}
		else if (lado == "2") {
			JugadorIzq = true;
			break;
		}
		system("cls");
	}
}

void PrintTable() {

	if (PosJD != -1 && PosJD!=11) {
		EstadoCasD[PosJD] = true;
	}
	if (PosJI != -1&& PosJI!=11) {
		EstadoCasI[PosJI] = true;
	}
	for (int i = 0; i < 6; i++) {
		for (int j = 0; j < 24;j++) {
			if (i==3 && j==0) {
				if (PosJI == -1) {
					cout << "[I .]";
				}
				else {
					cout << "[ I ]";
				}
			}
			else if (i == 2 && j == 2) {
				if (EstadoCasI[0] == true) {
					if (PosJI == 0) {
						(CasillasI[0] <= 9) ? cout << "["<<CasillasI[0]<< " .]" : cout << "[" << CasillasI[0]<<".]";
					}
					else {
						(CasillasI[0] <= 9) ? cout << "[" << CasillasI[0]<< "  ]" : cout << "[" << CasillasI[0]<<" ]";
					}
					
				}
				else
				{
					cout << "[ ? ]";
				}
			}
			else if (i == 4 && j == 2) {
				if (EstadoCasI[1] == true) {
					if (PosJI == 1) {
						(CasillasI[1] <= 9) ? cout << "[" << CasillasI[1] << " .]": cout << "[" << CasillasI[1] << ".]";
					}
					else {
						(CasillasI[1] <= 9) ? cout << "[" << CasillasI[1] << "  ]": cout << "[" << CasillasI[1]<< " ]";
					}
				}
				else
				{
					cout << "[ ? ]";
				}
			}
			else if (i == 1 && j == 4) {
				if (EstadoCasI[2] == true) {
					if (PosJI == 2) {
						(CasillasI[2] <= 9) ? cout << "[" << CasillasI[2] << " .]": cout << "[" << CasillasI[2] << ".]";
					}
					else {
						(CasillasI[2] <= 9) ? cout << "[" << CasillasI[2] << "  ]": cout << "[" << CasillasI[2] << " ]";
					}
				}
				else
				{
					cout<< "[ ? ]";
				}
			}
			else if (i == 3 && j == 4) {
				if (EstadoCasI[3] == true) {
					if (PosJI == 3) {
						(CasillasI[3] <= 9) ? cout << "[" << CasillasI[3]<< " .]" : cout << "[" << CasillasI[3] << ".]";
					}
					else {
						(CasillasI[3] <= 9) ? cout << "[" << CasillasI[3] << "  ]": cout << "[" << CasillasI[3] << " ]";
					}
				}
				else
				{
					cout<< "[ ? ]";
				}
			}
			else if (i == 5 && j == 4) {
				if (EstadoCasI[4] == true) {
					if (PosJI == 4) {
						(CasillasI[4] <= 9) ? cout << "[" << CasillasI[4] << " .]": cout << "[" << CasillasI[4] << ".]";
					}
					else {
						(CasillasI[4] <= 9) ? cout << "[" << CasillasI[4]<< "  ]" : cout << "[" << CasillasI[4] << " ]";
					}
				}
				else
				{
					cout<< "[ ? ]";
				}
			}
			else if (i == 1 && j == 6) {
				if (EstadoCasI[5] == true) {
					if (PosJI == 5) {
						(CasillasI[5] <= 9) ? cout << "[" << CasillasI[5] << " .]": cout << "[" << CasillasI[5] << ".]";
					}
					else {
						(CasillasI[5] <= 9) ? cout << "[" << CasillasI[5] << "  ]": cout << "[" << CasillasI[5] << " ]";
					}
				}
				else
				{
					cout<< "[ ? ]";
				}
			}
			else if (i == 3 && j == 6) {
				if (EstadoCasI[6] == true) {
					if (PosJI == 1) {
						(CasillasI[6] <= 9) ? cout << "[" << CasillasI[6] << " .]": cout << "[" << CasillasI[6] << ".]";
					}
					else {
						(CasillasI[6] <= 9) ? cout << "[" << CasillasI[6] << "  ]": cout << "[" << CasillasI[6] << " ]";
					}
				}
				else
				{
					cout<< "[ ? ]";
				}
			}
			else if (i == 5 && j == 6) {
				if (EstadoCasI[7] == true) {
					if (PosJI == 7) {
						(CasillasI[7] <= 9) ? cout << "[" << CasillasI[7] << " .]": cout << "[" << CasillasI[7] << ".]";
					}
					else {
						(CasillasI[7] <= 9) ? cout << "[" << CasillasI[7]<< "  ]" : cout << "[" << CasillasI[7] << " ]";
					}
				}
				else
				{
					cout<< "[ ? ]";
				}
			}
			else if (i == 1 && j == 8) {
				if (EstadoCasI[8] == true) {
					if (PosJI == 8) {
						(CasillasI[8] <= 9) ? cout << "[" << CasillasI[8] << " .]" : cout << "[" << CasillasI[8] << ".]";
					}
					else {
						(CasillasI[8] <= 9) ? cout << "[" << CasillasI[8] << "  ]" : cout << "[" << CasillasI[8] << " ]";
					}
				}
				else
				{
					cout<< "[ ? ]";
				}
			}
			else if (i == 3 && j == 8) {
				if (EstadoCasI[9] == true) {
					if (PosJI == 9) {
						(CasillasI[9] <= 9) ? cout << "[" << CasillasI[9] << " .]": cout << "[" << CasillasI[9] << ".]";
					}
					else {
						(CasillasI[9] <= 9) ? cout << "[" << CasillasI[9] << "  ]": cout << "[" << CasillasI[9] << " ]";
					}
				}
				else
				{
					cout<< "[ ? ]";
				}
			}
			else if (i == 5 && j == 8) {
				if (EstadoCasI[10] == true) {
					if (PosJI == 10) {
						(CasillasI[10] <= 9) ? cout << "[" << CasillasI[10] << " .]": cout  << CasillasI[10] << ".]";
					}
					else {
						(CasillasI[10] <= 9) ? cout << "[" << CasillasI[10] << "  ]": cout  << CasillasI[10] << " ]";
					}
				}
				else
				{
					cout<< "[ ? ]";
				}
			}
			else if (i == 3 && j == 10) {
				cout << "  F  ";
			}
			else if (i == 3 && j == 11) {
				cout << "  I  ";
			}
			else if (i == 3 && j == 12) {
				cout << "  N  ";
			}
			else if (i == 1 && j ==14) {
			if (EstadoCasD[8] == true) {
				if (PosJD == 8) {
					(CasillasD[8] <= 9) ? cout << "[" << CasillasD[8]<< " ,]" : cout << "[" << CasillasD[8] << ",]";
				}
				else {
					(CasillasD[8] <= 9) ? cout << "[" << CasillasD[8] << "  ]": cout << "[" << CasillasD[8] << " ]";
				}
			}
			else
			{
				cout<< "[ ? ]";
			}
			}
			else if (i == 3 && j == 14) {
			if (EstadoCasD[9] == true) {
				if (PosJD == 9) {
					(CasillasD[9] <= 9) ? cout << "[" << CasillasD[9] << " ,]": cout << "[" << CasillasD[9] << ",]";
				}
				else {
					(CasillasD[9] <= 9) ? cout << "[" << CasillasD[9] << "  ]": cout << "[" << CasillasD[9] << " ]";
				}
			}
			else
			{
				cout<< "[ ? ]";
			}
			}
			else if (i == 5 && j == 14) {
			if (EstadoCasD[10] == true) {
				if (PosJD == 10) {
					(CasillasD[10] <= 9) ? cout << "[" << CasillasD[10] << " ,]": cout << "[" << CasillasD[10] << ",]";
				}
				else {
					(CasillasD[10] <= 9) ? cout << "[" << CasillasD[10] << "  ]": cout << "[" << CasillasD[10] << " ]";
				}
			}
			else
			{
				cout<< "[ ? ]";
			}
			}
			else if (i == 1 && j == 16) {
			if (EstadoCasD[5] == true) {
				if (PosJD == 5) {
					(CasillasD[5] <= 9) ? cout << "[" << CasillasD[5] << " ,]": cout << "[" << CasillasD[5] << ",]";
				}
				else {
					(CasillasD[5] <= 9) ? cout << "[" << CasillasD[5] << "  ]": cout << "[" << CasillasD[5] << " ]";
				}
			}
			else
			{
				cout<< "[ ? ]";
			}
			}
			else if (i == 3 && j == 16) {
			if (EstadoCasD[6] == true) {
				if (PosJD == 6) {
					(CasillasD[6] <= 9) ? cout << "[" << CasillasD[6] << " ,]": cout << "[" << CasillasD[6] << ",]";
				}
				else {
					(CasillasD[6] <= 9) ? cout << "[" << CasillasD[6] << "  ]": cout << "[" << CasillasD[6] << " ]";
				}
			}
			else
			{
				cout<< "[ ? ]";
			}
			}
			else if (i == 5 && j == 16) {
			if (EstadoCasD[7] == true) {
				if (PosJD == 7) {
					(CasillasD[7] <= 9) ? cout << "[" << CasillasD[7] << " ,]": cout << "[" << CasillasD[7] << ",]";
				}
				else {
					(CasillasD[7] <= 9) ? cout << "[" << CasillasD[7] << "  ]": cout << "[" << CasillasD[7] << " ]";
				}
			}
			else
			{
				cout<< "[ ? ]";
			}
			}
			else if (i == 1 && j == 18) {
			if (EstadoCasD[2] == true) {
				if (PosJD == 2) {
					(CasillasD[2] <= 9) ? cout << "[" << CasillasD[2] << " ,]": cout << "[" << CasillasD[2] << ",]";
				}
				else {
					(CasillasD[2] <= 9) ? cout << "[" << CasillasD[2] << "  ]": cout << "[" << CasillasD[2] << " ]";
				}
			}
			else
			{
				cout<< "[ ? ]";
			}
			}
			else if (i == 3 && j == 18) {
			if (EstadoCasD[3] == true) {
				if (PosJD == 3) {
					(CasillasD[3] <= 9) ? cout << "[" << CasillasD[3] << " ,]": cout << "[" << CasillasD[3] << ",]";
				}
				else {
					(CasillasD[3] <= 9) ? cout << "[" << CasillasD[3] << "  ]": cout << "[" << CasillasD[3] << " ]";
				}
			}
			else
			{
				cout<< "[ ? ]";
			}
			}
			else if (i == 5 && j == 18) {
			if (EstadoCasD[4] == true) {
				if (PosJD == 4) {
					(CasillasD[4] <= 9) ? cout << "[" << CasillasD[4] << " ,]": cout << "[" << CasillasD[4] << ",]";
				}
				else {
					(CasillasD[4] <= 9) ? cout << "[" << CasillasD[4] << "  ]": cout << "[" << CasillasD[4] << " ]";
				}
			}
			else
			{
				cout<< "[ ? ]";
			}
			}
			else if (i == 2 && j == 20) {
			if (EstadoCasD[0] == true) {
				if (PosJD == 0) {
					(CasillasD[0] <= 9) ? cout << "[" << CasillasD[0]<< " ,]" : cout << "[" << CasillasD[0] << ",]";
				}
				else {
					(CasillasD[0] <= 9) ? cout << "[" << CasillasD[0] << "  ]": cout << "[" << CasillasD[0] << " ]";
				}
			}
			else
			{
				cout<< "[ ? ]";
			}
			}
			else if (i == 4 && j == 20) {
			if (EstadoCasD[1] == true) {
				if (PosJD == 1) {
					(CasillasD[1] <= 9) ? cout << "[" << CasillasD[1] << " ,]": cout << "[" << CasillasD[1] << ".]";
				}
				else {
					(CasillasD[1] <= 9) ? cout << "[" << CasillasD[1] << "  ]": cout << "[" << CasillasD[1] << " ]";
				}
			}
			else
			{
				cout<< "[ ? ]";
			}
			}
			else if (i == 3 && j == 22) {
				if (PosJD == -1) {
					cout << "[D ,]";
				}
				else {
					cout << "[ D ]";
				}
			}
			else {
				cout << "     ";
			}
		}
		cout << endl;
	}
}

void GenerarNumeros() {
	for (int i = 0; i < 11; i++) {
		NumPool.push_back(2 + rand() % (20 - 2));
	}
}

void LLenarPos(int i) {
	int num = rand() % (11);
	while (true) {
		if (EstadoCasD[num] == true) {
			num = rand() % 11;
			continue;
		}
		else {
			if (i < 2) {
				EstadoCasD[num] = true;
			}
			CasillasD[num] = NumPool[i];
			break;
		}
	}
	num = rand() % (11);
	while (true) {
		if (EstadoCasI[num] == true) {
			num = rand() % 11;
			continue;
		}
		else {
			if (i < 2) {
				EstadoCasI[num] = true;
			}
			CasillasI[num] = NumPool[i];
			break;
		}
	}

}

void OrganizarNum() {
	for (int i = 0; i < 11; i++) {
		
		LLenarPos(i);
	}
}

void GenerarBomba() {
	int num;
	while (true) {
		
		num = rand() % (10);
		if (EstadoCasD[num] == false && EstadoCasI[num] == false) {
			CasillasD[num] = 99;
			CasillasI[num] = 99;
			break;
		}
		else {
			continue;
		}
		

	}
}

void gotoxy(int x, int y) {
	HANDLE hcon;
	hcon = GetStdHandle(STD_OUTPUT_HANDLE);
	COORD dwPos;
	dwPos.X = x;
	dwPos.Y = y;
	SetConsoleCursorPosition(hcon, dwPos);
}