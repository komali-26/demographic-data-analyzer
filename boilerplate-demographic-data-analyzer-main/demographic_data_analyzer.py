import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load dataset
    df = pd.read_csv("adult.data.csv")

    # 1. Number of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    # 4. Percentage with advanced education earning >50K
    higher_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])

    higher_edu_rich = round(
        (df[higher_edu]['salary'] == '>50K').mean() * 100, 1
    )

    # 5. Percentage without advanced education earning >50K
    lower_edu_rich = round(
        (df[~higher_edu]['salary'] == '>50K').mean() * 100, 1
    )

    # 6. Minimum work hours per week
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage of rich among those who work minimum hours
    min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = round(
        (min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # 8. Country with highest percentage of people earning >50K
    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total = df['native-country'].value_counts()

    country_percent = (country_salary / country_total) * 100

    highest_earning_country = country_percent.idxmax()
    highest_earning_country_percentage = round(country_percent.max(), 1)

    # 9. Most popular occupation for those earning >50K in India
    india_rich = df[
        (df['native-country'] == 'India') &
        (df['salary'] == '>50K')
    ]

    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # Optional print (for debugging)
    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Higher education rich:", higher_edu_rich)
        print("Lower education rich:", lower_edu_rich)
        print("Min work hours:", min_work_hours)
        print("Rich % among min workers:", rich_percentage)
        print("Highest earning country:", highest_earning_country)
        print("Highest earning country %:", highest_earning_country_percentage)
        print("Top occupation in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }