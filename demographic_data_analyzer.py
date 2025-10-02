# Importa a biblioteca pandas, que é usada para manipulação e análise de dados
import pandas as pd

# Define uma função que calcula diversas estatísticas demográficas a partir de um arquivo CSV
def calculate_demographic_data(print_data=True):
    # Lê os dados do arquivo 'adult.data.csv' e armazena em um DataFrame do pandas
    df = pd.read_csv('adult.data.csv')  # substitua pelo caminho correto do CSV

    # 1. Contagem de indivíduos por raça
    # Usa value_counts() para contar quantas vezes cada valor aparece na coluna 'race'
    # O resultado é uma série do pandas com as raças como índice e as contagens como valores
    race_count = df['race'].value_counts()

    # 2. Idade média dos homens
    # Primeiro filtra apenas os registros em que 'sex' é 'Male'
    # Depois calcula a média da coluna 'age' e arredonda para 1 casa decimal
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentual de pessoas com grau de Bachelors
    # Compara cada valor da coluna 'education' com 'Bachelors', obtendo True/False
    # Calcula a média desses valores booleanos (True=1, False=0) e multiplica por 100
    # Arredonda para 1 casa decimal
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Percentual de pessoas com educação avançada que ganham >50K
    # Educação avançada inclui Bachelors, Masters e Doctorate
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    # Pessoas sem educação avançada
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Percentual de pessoas com educação avançada que ganham mais de 50K
    higher_education_rich = round((higher_education['salary'] == '>50K').mean() * 100, 1)
    # Percentual de pessoas sem educação avançada que ganham mais de 50K
    lower_education_rich = round((lower_education['salary'] == '>50K').mean() * 100, 1)

    # 5. Número mínimo de horas trabalhadas por semana
    # Usa min() para encontrar o menor valor na coluna 'hours-per-week'
    min_work_hours = df['hours-per-week'].min()

    # 6. Percentual de pessoas que trabalham o mínimo de horas e ganham >50K
    # Filtra os indivíduos que trabalham o mínimo de horas
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    # Calcula o percentual desses indivíduos que têm salário >50K
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # 7. País com maior percentual de pessoas que ganham >50K
    # Filtra as pessoas que ganham >50K, conta por país, e divide pela contagem total de pessoas por país
    # Multiplica por 100 para obter percentual
    country_salary = (df[df['salary'] == '>50K']['native-country'].value_counts() /
                      df['native-country'].value_counts() * 100)
    # Identifica o país com maior percentual
    highest_earning_country = country_salary.idxmax()
    # Percentual correspondente ao país
    highest_earning_country_percentage = round(country_salary.max(), 1)

    # 8. Ocupação mais popular entre os que ganham >50K na Índia
    # Filtra pessoas com 'native-country' igual a 'India' e salário >50K
    # Usa mode() para encontrar a ocupação mais frequente e pega o primeiro valor
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # Exibe os resultados, caso print_data seja True
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    # Retorna os resultados em um dicionário
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
