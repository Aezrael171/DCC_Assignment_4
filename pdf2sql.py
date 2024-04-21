import fitz  
import csv

def read_pdf_and_write_to_csv(pdf_file, csv_file):
    with fitz.open(pdf_file) as pdf_document:
        with open(csv_file, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            
            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)
                text = page.get_text()
                
                lines = text.split('\n')
                
                for line in lines:
                    csv_writer.writerow([line])

def csv_to_sql_dump(csv_file, sql_file, table_name):

    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        

        with open(sql_file, 'w', encoding='utf-8') as sqlfile:

            for row in csv_reader:

                values = ','.join(f'"{value}"' for value in row)
                sql_statement = f'INSERT INTO {table_name} VALUES ({values});\n'

                sqlfile.write(sql_statement)

pdf_file = 'redemption.pdf'
csv_file = 'redemption.csv'
read_pdf_and_write_to_csv(pdf_file, csv_file)

sql_file = 'redemption.sql'
table_name = 'redemption'

csv_to_sql_dump(csv_file, sql_file, table_name)
