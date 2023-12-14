#Importing Pandas

import pandas

#Build Pandas Dataframe

fruit_sales = pandas.DataFrame({'Apples': [35,41 ], 
              'Bananas': [21, 34]},
             index=['2017 Sales', '2018 Sales'])

#Write Pandas Dataframe to file fruit.csv

fruit_sales.to_csv("fruit.csv")

 

