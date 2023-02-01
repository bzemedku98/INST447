import pandas as pd

pd.read_csv('data/trict_or_treat.csv')

ld = [{'age_group' : 'toddler', 'costume' : 'wonder-woman', 'candy' : 'kitkat'},
        {'age_group' : 'grade-school','costume' : 'Elsa', 'candy' : 'skittles'},
        {'age_group' : 'pre-school','costume' : 'Wolverine', 'candy' : 'peanut M&Ms'}]

dataframe = pd.DataFrame(ld)

# dataframe.to_csv('data/trict_or_treat.csv')