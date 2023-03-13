import pandas as pd
from user_questions import get_quality_input, get_quantity_input

# Import the database from .csv file and assign a name
diamanti = pd.read_csv('table.csv')

# Drop useless table
diamanti = diamanti.drop('depth', axis=1)
diamanti = diamanti.drop('color', axis=1)
diamanti = diamanti.drop('table', axis=1)

# Rename few columns
diamanti = diamanti.rename(columns={'cut':'cut-quality', 'x': 'lenght', 'y':'width', 'z':'depths'}) 

# function to define the list of columns
colonne = diamanti.columns
def conteggio(x):
    for col in x:
        print(col.title())

# Fix the price column
diamanti['price'] = diamanti['price'].astype(str) + ' $'



# Print the names of the columns
print(f"\nThis is a table containing {len(colonne)} columns named:\n")
conteggio(colonne)

# Get user input
quality_input = get_quality_input()
quantity_input = get_quantity_input()


# define the quality preferred by the user
user_preferred_quality = diamanti[diamanti['cut-quality']== quality_input.title()]

# The best diamond is:
print("\nThe best of the list is:")
print(user_preferred_quality.sort_values('carat', ascending=False,).head(int(quantity_input)))
print('\n')