#include <iostream>
#include <fstream>
#include <cstdlib>

int main() {
    std::string remoteServer = "adres_serwera";
    std::string username = "uzytkownik";
    std::string password = "haslo";

    std::string commands[] = {
            "ls -l", // Listowanie plików
            "ps aux" // Listowanie procesów
    };

    // Wykonanie poleceń i zapis wyników do pliku
    std::ofstream outputFile("wyniki.txt");
    for (const auto& cmd : commands) {
        std::string fullCommand = "ssh " + username + "@" + remoteServer + " '" + cmd + "'";
        std::string result = std::system(fullCommand.c_str());
        outputFile << "Wynik polecenia '" << cmd << "':\n" << result << "\n\n";
    }
    outputFile.close();

    std::cout << "Wyniki zostały zapisane do pliku wyniki.txt.\n";
    return 0;
}
