import csv


class dataLine():
    def __init__(self, data):
        self.data = data
        self.date = data[0]
        self.temp_media = data[1]
        self.temp_min = data[2]
        self.temp_max = data[3]
        self.precipitacao = data[4]
        self.final_de_semana = data[5]
        self.consumo_de_cerveja = data[6]

    def __str__(self):
        return ("----------------------------------------------------------"
                f"Data: {self.date}, Temperatura Média: {self.temp_media},\n"
                f"Temperatura Mínima: {self.temp_min}\n"
                f"Temperatura Máxima: {self.temp_max}\n"
                f"Precipitação: {self.precipitacao}\n"
                f"Final de Semana: {self.final_de_semana}\n"
                f"Consumo de Cerveja: {self.consumo_de_cerveja}\n"
                "---------------------------------------------------------")


def abrirCSV():
    data = []

    with open("Consumo_cerveja.csv", mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] != '':
                line = ([
                    row[0],
                    float(row[1].replace(",", ".")),
                    float(row[2].replace(",", ".")),
                    float(row[3].replace(",", ".")),
                    float(row[4].replace(",", ".")),
                    int(row[5].replace(".", "")),
                    int(row[6].replace(".", ""))
                ])
                appendedLine = dataLine(line)
                data.append(appendedLine)
            else:
                break

    return data


def menu(data):
    while True:
        try:
            choice = int(input("Escolha uma opção: \n"
                               "------------------------------------------\n"
                               "1 - Dados de um data.\n"
                               "2 - Media de consumo em um mês.\n"
                               "3 - Media de consuno no final de semana"
                               " em um mês.\n"
                               "0 - Sair\n"
                               "------------------------------------------\n"
                               "Opção: "))
            if choice == 1:
                date = input("----------------------------------------------\n"
                             "Digite a data no formato dd/mm/yyyy: ")
                dateSearch(data, date)
            elif choice == 2:
                averageConsMonth(data)
            elif choice == 3:
                weekendConsMonth(data)
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
            elif choice == 0:
                break
            else:
                print("Opção inválida. Tente novamente.")
                menu()
        except ValueError:
            print("Opção inválida. Tent novamente.")


def dateSearch(data, date):

    sdate = date.split("/")
    date = f"{sdate[2]}-{sdate[1]}-{sdate[0]}"
    for line in data:
        if line.date == date:
            return print(line.__str__())

    return print("Data não encontrada. Digit uma data de 01/01/2015 até"
                 "31/12/2015")


def averageConsMonth(data):
    dayscomsuption = []
    while True:
        try:
            choice = int(input("-------------------------------------------\n"
                               "Digite o mês que deseja saber a média de "
                               "consumo de cerveja: "))
            if choice < 1 or choice > 12:
                print("Mês inválido. Tente novamente.")
                averageConsMonth(data)
            else:
                for line in data:
                    if int(line.date.split("-")[1]) == choice:
                        dayscomsuption.append(line.consumo_de_cerveja)

            avg_consumption = sum(dayscomsuption) / len(dayscomsuption)
            return print("--------------------------------------------------\n"
                         "A média de consumo de cerveja por dia "
                         f"no mês {choice} foi de {avg_consumption}"
                         "---------------------------------------------------")

        except ValueError:
            print("Mês inválido. Tente novamente.")


def weekendConsMonth(data):
    dayscomsuption = []
    while True:
        try:
            choice = int(input("-------------------------------------------\n"
                               "Digite o mês que deseja saber a média de "
                               "consumo de cerveja: "))
            if choice < 1 or choice > 12:
                print("Mês inválido. Tente novamente.")
                weekendConsMonth(data)
            else:
                for line in data:
                    if (int(line.date.split("-")[1]) == choice and
                            line.final_de_semana == 1):
                        dayscomsuption.append(line.consumo_de_cerveja)

            avg_consumption = sum(dayscomsuption) / len(dayscomsuption)
            return print("--------------------------------------------------\n"
                         "A média de consumo de cerveja por dia no fim de "
                         f"semana no mês {choice} foi de {avg_consumption}"
                         "---------------------------------------------------")
        except ValueError:
            print("Mês inválido. Tente novamente.")


def main():
    data = abrirCSV()
    menu(data)


if __name__ == "__main__":
    main()
