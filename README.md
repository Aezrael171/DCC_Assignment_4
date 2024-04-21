## DCC ASSIGNMENT 4 
### Name : Arjun B Dikshit
### Roll no. 23110040

To set up locally,just clone the repo. Import redemption.sql (which has its own target schema) into your sql workbench with the name redemption,
and run app.py file in terminal

How the website was made,
The website is made using Flask CSS HTML and JS 

1. PDF TO CSV CONVERSION
First, using a python file, where fitz was used to read the pdf file and extract the table and csv writer was used to write the table one by one into the csv file, which was then exported.
THen csv file was converted to sql dump in a similar way and was imported into  a database. The corresponding code is given in the pdf2sql file in the code
3. Designing the Interface.
   a) The main page UI
   ![image](https://github.com/Aezrael171/DCC_Assignment_4/assets/166854755/3628c7e8-7dd3-4ac4-b56e-79cb2598d629)
   The main page UI was designed using HTML Bootstrap and Custom CSS combined. The main page has an app route ('/')
   index.html has files for multiple other web pages, neatly arranged in divs with their own style. Each box corresponds to each question

   ##### QUESTION 1:
   The UI was made using the above mentioned tools. The second dropdown is disabled until you select the table that you want to scan. THis dynamic dropdown was implemented using javascript. Also if you submit an incorrect query, it says no data found.
   
   Select the bond finder section
   EMPTY SEARCH
   This should be the page that you get after selecting the bond finder.
   ![image](https://github.com/Aezrael171/DCC_Assignment_4/assets/166854755/2e828e25-e12f-4937-8ccf-689a16511a71)
   
   First, select the table that you want to filter with using the dropdown menu
   ![image](https://github.com/Aezrael171/DCC_Assignment_4/assets/166854755/e753dfe3-4a6f-47dc-b419-83cc2e907fa3)

   Then Select the column that you want to filter the data by:
   ![image](https://github.com/Aezrael171/DCC_Assignment_4/assets/166854755/cdc2208e-fc00-4098-a81c-546d0a560f40)

   Search for the required data and hit search
   ![image](https://github.com/Aezrael171/DCC_Assignment_4/assets/166854755/f03c5a97-7a5f-4085-8d2c-6e69a16c5631)

   Your results should appear
   ![image](https://github.com/Aezrael171/DCC_Assignment_4/assets/166854755/94eac730-f93b-48ec-910d-f5761a346c69)

   ##### QUESTION 2
   You can search your query using the search box. The bar graphs are made using chart.js, while the table is rendered. There are also download options at the end to save the files locally on your computer
   Select the company or individual bond tracker section.
   ![image](https://github.com/Aezrael171/DCC_Assignment_4/assets/166854755/c1c4e849-479d-4cc5-945e-c4da0fd33689)

   Fill the search bar with the required Query, and You should get the two bar plots as well as the option to save the plots
   ![image](https://github.com/Aezrael171/DCC_Assignment_4/assets/166854755/e7ae1147-0c80-4044-8c9b-6bc34284bc59)

   #### QUESTION 3
   You can search your query using the search box. The bar graphs are made using chart.js, while the table is rendered. There are also download options at the end to save the files locally on your computer
   Select the party bond tracker section.
   ![image](https://github.com/Aezrael171/DCC_Assignment_4/assets/166854755/501caa54-9547-4da6-bb57-2be662ca3a17)


   Fill the search bar with the required Query, and You should get the two bar plots as well as the option to save the plots
   ![image](https://github.com/Aezrael171/DCC_Assignment_4/assets/166854755/417262b6-5100-4451-859d-62c6196d58f6)

   ##### QUESTION 4
   You can select the political party to understand which companies the party has purchased electoral bonds from  and analyse accordingly. You can also view an alluvial chart plotted using external library anychart and javascript in html code. the alluvial chart also ha a feature of showing the data as you hover over it. You can also download the plot
   
   Select which political party you want to searh the data of, and hit submit. You will receive a dataset with an alluvial plot.
   ![image](https://github.com/Aezrael171/DCC_Assignment_4/assets/166854755/18d51b8c-b1df-404a-a395-b9f2dce5ba50)
   ![image](https://github.com/Aezrael171/DCC_Assignment_4/assets/166854755/5824f612-3174-420c-a43a-123e6a40ed59)
   ![image](https://github.com/Aezrael171/DCC_Assignment_4/assets/166854755/78d1642b-6d2d-47ff-8f3a-7eec56c09175)

   ##### QUESTION 5
   You can select the company to understand which parties have purchased from the company and analyse accordingly. You can also view an alluvial chart plotted using external library anychart and javascript in html code. the alluvial chart also ha a feature of showing the data as you hover over it. You can also download the plot
   
   Select which political party you want to searh the data of, and hit submit. You will receive a dataset with an alluvial plot.
   ![image](https://github.com/Aezrael171/DCC_Assignment_4/assets/166854755/53da62b8-b93b-44da-a64b-eb469276992a)
   ![image](https://github.com/Aezrael171/DCC_Assignment_4/assets/166854755/5b3af517-b112-49da-99fd-c52737503b18)
   ![image](https://github.com/Aezrael171/DCC_Assignment_4/assets/166854755/ce980806-bde9-45e8-808e-6911a0c3308b)

   #### QUESTION 6
   Select the PI chart section to view (and  download) the pie chart showing each part's percentage of electoral bonds purchased. You can hover over each section of the pie chart to view each part of the pie chart and view the party and number of donations. It also has a feature to download the pie chart 

   ![image](https://github.com/Aezrael171/DCC_Assignment_4/assets/166854755/49c96d22-343e-4b99-a205-e1f72b1c695b)
   ![image](https://github.com/Aezrael171/DCC_Assignment_4/assets/166854755/53f976a4-1484-48ab-8ee7-1f817c9a375f)





