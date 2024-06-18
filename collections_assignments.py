# Retrieve the 'G' from following list using positive indexing
L1 = [1, 2, 'hi', (21, 78, [-2, -4, ('Bahubali', 'KGF', 'RRR')])]
print(L1[3][2][2][1][1])
print()
# Retrieve the 22 from following tuple using negative index
T1 = (1, 2, 'hi', (21, 78, [-2, -4, (200, 400, [11, 22, 300])]))
print(T1[-1][-1][-1][-1][-2])
print()
"""
Retrieve 'G' from last_name using following dictionary with negative indexing
Retrieve 3000 from salaries using following dictionary with positive indexing
Retrieve 50 from Age using following dictionary with negative indexing
"""
D1 = {'names': [{'first_name': 'Anilkumar', 'last_name': 'Para'},
                {'first_name': 'Sachin', 'last_name': 'Tendulkar'},
                {'first_name': 'Mahesh', 'last_name': 'G'}],
      'Salaries': [2000, 3000, 4000],
      'Age': (35, 50, 47)
      }

print(D1["names"][-1]["last_name"])
print(D1["Salaries"][1])
print(D1["Age"][-2])
print()

"""
retrieve the abbreviation of "California" state using positive indexing
retrieve the Alabama state 3rd area code using negative indexing
retrieve the Arizona state name using positive indexing
"""

usa_states_info = {"states": [
    {
      "name": "Alabama",
      "abbreviation": "AL",
      "area_codes": ["205", "251", "256", "334", "938"]
    },
    {
      "name": "Alaska",
      "abbreviation": "AK",
      "area_codes": ["907"]
    },
    {
      "name": "Arizona",
      "abbreviation": "AZ",
      "area_codes": ["480", "520", "602", "623", "928"]
    },
    {
      "name": "Arkansas",
      "abbreviation": "AR",
      "area_codes": ["479", "501", "870"]
    },
    {
      "name": "California",
      "abbreviation": "CA",
      "area_codes": ["209", "213", "310", "323", "408", "415", "424", "442", "510", "530", "559", "562", "619", "626", "628", "650", "657", "661", "669", "707", "714", "747", "760", "805", "818", "831", "858", "909", "916", "925", "949", "951"]
    }
    ]
}
print(usa_states_info["states"][4]["abbreviation"])
print(usa_states_info["states"][-5]["area_codes"][-3])
print(usa_states_info["states"][2]["name"])
